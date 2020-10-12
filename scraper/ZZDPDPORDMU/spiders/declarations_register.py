import scrapy


def get_main_table_row_data(response, row):
    return response.xpath('//table/tr[%s]/td/text()' % row).get()


def parse_raw_amount(raw_amount):
    if raw_amount is None:
        return None
    tokens = ['с ДДС', 'лв.', 'лв', 'лева', ' ', ' ']
    clean_amount = raw_amount
    for token in tokens:
        clean_amount = clean_amount.replace(token, '').strip()
    if clean_amount is '':
        return None

    return int(float(clean_amount.replace(',', '.')))


class DeclarationsRegisterSpider(scrapy.Spider):
    name = 'declarations_register'
    start_urls = [
        'http://212.122.186.189:800/Register-7a-2020.jsp/'
    ]

    def parse(self, response):
        # deduplicate the multiple links to a same page using set()
        all_page_urls = list(set(response.xpath('//a/@href').getall()))
        for page_url in all_page_urls:
            yield response.follow(page_url, self.parse_declaration_page)

    def parse_declaration_page(self, response):
        return {
            "legal_entity_name": get_main_table_row_data(response, 1),
            "legal_entity_id": get_main_table_row_data(response, 2),
            "public_company": get_main_table_row_data(response, 3),
            "media_service_type": get_main_table_row_data(response, 4),
            "media_service_name": get_main_table_row_data(response, 5),
            "real_owner": get_main_table_row_data(response, 6),
            "executive_individual": get_main_table_row_data(response, 7),
            "contracts": self.parse_contracts(response)
        }

    @staticmethod
    def parse_contracts(response):
        contracts = []
        # [position()>1] is used to skip first one (header row)
        for row in response.xpath('//table//table//tr[position()>1]'):
            contract_amount_raw = row.xpath('./td[1]/text()').get()
            contracts.append({
                "contract_amount_raw": contract_amount_raw,
                "contract_amount": parse_raw_amount(contract_amount_raw),
                "contract_basis_raw": row.xpath('./td[2]/text()').get(),
                "contract_sponsor_raw": row.xpath('./td[3]/text()').get(),
            })
        return contracts


EXAMPLE_ITEM_STRUCTURE = {
    # "Юридическо лице"
    "legal_entity_name": "АБ КОМЮНИКЕЙШЪНС ЕООД",
    # ЕИК
    "legal_entity_id": "200964424",
    # Публично дружество
    "public_company": "неприложимо",
    # Тип на медийната услуга
    "media_service_type": "Печатна медия; Онлайн новинарско издание",
    # Наименование на медийната услуга
    "media_service_name": "Списание Агрозона; www.agrozona.bg",
    # Действителен собственик на доставчика на медийната услуга (ДМУ)
    "real_owner": "Ивайло Димитров Тодоров",
    # Лице с фактически контрол
    "executive_individual": "неприложимо",

    # Договори по чл. 7а, ал. 4
    "contracts": [
        {
            # "Стойност на договора" в суров вид, както са го нащракали чиновниците.
            # Напр. "80250" или "4200 лв. с ДДС" или "1907,82" и др.
            "contract_amount_raw": "4200 лв. с ДДС",
            # Жалък опит за parse
            "contract_amount": 4200,
            # "Основание" в суров вид
            "contract_basis_raw": "10.04.2019 Публикуване на инф. материали",
            # "Поръчител" в суров вид
            "contract_sponsor_raw": "ДКИ КУЛТУРЕН ЦЕНТЪР ДВОРЕЦА/124609886",
        }
    ]
}
