import requests
from lxml import etree as ET

from odoo import api, fields, models


class Calculator(models.Model):
    _name = 'calculator.calculator'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Float("Answer")
    no1 = fields.Float("Number 1")
    no2 = fields.Float("Number 2")
    action = fields.Selection(
        [('add', "Add"), ('sub', "Substraction"), ('divide', "Division"), ('multiply', "Multiply")],default='add')

    def calculate(self):
        url = "http://www.dneonline.com/calculator.asmx"
        if self.action == 'add':
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
                                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                                      <soap:Body>
                                        <Add xmlns="http://tempuri.org/">
                                          <intA>{str(int(self.no1))}</intA>
                                          <intB>{str(int(self.no2))}</intB>
                                        </Add>
                                      </soap:Body>
                                    </soap:Envelope>            
                        """
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': 'http://tempuri.org/Add'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            res = ET.fromstring(response.content)
            for add_res in res:
                children = add_res.getchildren()
                for result in children:
                    child = result.getchildren()
                    self.name = float(child[0].text)
        elif self.action == 'sub':
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
                            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                              <soap:Body>
                                <Subtract xmlns="http://tempuri.org/">
                                  <intA>{str(int(self.no1))}</intA>
                                  <intB>{str(int(self.no2))}</intB>
                                </Subtract>
                              </soap:Body>
                            </soap:Envelope>            
            """
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': 'http://tempuri.org/Subtract'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            res = ET.fromstring(response.content)
            for sub_res in res:
                children = sub_res.getchildren()
                for result in children:
                    child = result.getchildren()
                    self.name = float(child[0].text)
        elif self.action == 'multiply':
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                          <soap:Body>
                            <Multiply xmlns="http://tempuri.org/">
                              <intA>{str(int(self.no1))}</intA>
                              <intB>{str(int(self.no2))}</intB>
                            </Multiply>
                          </soap:Body>
                        </soap:Envelope>            
            """
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': 'http://tempuri.org/Multiply'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            res = ET.fromstring(response.content)
            for mul_res in res:
                children = mul_res.getchildren()
                for result in children:
                    child = result.getchildren()
                    self.name = float(child[0].text)
        elif self.action == 'divide':
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
                            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                              <soap:Body>
                                <Divide xmlns="http://tempuri.org/">
                                  <intA>{str(int(self.no1))}</intA>
                                  <intB>{str(int(self.no2))}</intB>
                                </Divide>
                              </soap:Body>
                            </soap:Envelope>            
            """
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': 'http://tempuri.org/Divide'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            res = ET.fromstring(response.content)
            for div_res in res:
                children = div_res.getchildren()
                for result in children:
                    child = result.getchildren()
                    self.name = float(child[0].text)
