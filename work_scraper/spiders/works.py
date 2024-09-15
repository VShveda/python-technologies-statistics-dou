from typing import Generator

import scrapy
from scrapy.http import Response

from work_scraper.items import WorkScraperItem


class WorkSpider(scrapy.Spider):
    name = "works"
    allowed_domains = ["work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response: Response, **kwargs) -> Generator[Response, None, None]:
        jobs = response.css("h2.my-0 > a::attr(href)").getall()
        for job in jobs:
            job_url = response.urljoin(job)
            yield response.follow(job_url, callback=self.parse_job)

        next_page = response.css("li.no-style.add-left-default > a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    @staticmethod
    def parse_job(response: Response) -> Generator[WorkScraperItem, None, None]:
        item = WorkScraperItem()

        item["title"] = response.css("h1::text").get(default="-1").strip()

        company = (
            response.css("span.glyphicon-company + a > span.strong-500::text")
            .get(default="-1")
            .strip()
        )
        item["company"] = company

        salary = (
            response.css("li:nth-child(1) > span.strong-500::text")
            .get(default="-1")
            .strip()
            .replace(" ", "")
            .replace(" ", "")
        )
        item["salary"] = salary
        skills = response.css("ul.list-unstyled li span.ellipsis::text").getall()
        item["technologies"] = [skill.strip() for skill in skills if skill.strip()]

        description = response.css("div#job-description").get()

        if description:
            from scrapy.selector import Selector

            desc_selector = Selector(text=description)

            description_text = "\n".join(desc_selector.css("p::text").getall())
            description_list = "\n".join(desc_selector.css("ul li::text").getall())

            item["description"] = f"{description_text}\n{description_list}"
        else:
            item["description"] = "-1"

        print(f"Scraped item: {item}")
        yield item
