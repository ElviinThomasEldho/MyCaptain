import requests
from bs4 import BeautifulSoup
import pandas
import connect

s = requests.Session()
s.trust_env = False

page_url = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree"
req = requests.get(page_url)
content = req.content

soup = BeautifulSoup(content,"html.parser")
all_products = soup.find_all('a', class_='_31qSD5')
scraped_info_list = []

connect.connect()

for product in all_products:
    product_dict = {}
    product_dict["name"] = product.find('div', class_= '_3wU53n').text
    try:
        product_dict["rating"] = product.find('div', class_= 'hGSR34').text
    except AttributeError:
        product_dict["rating"] = ""
    product_dict["price"] = product.find('div', class_='_1vC4OE _2rQ-NK').text
    try:
        product_dict["discount"] = product.find('div', class_='VGWI6T').text
    except AttributeError:
        product_dict["discount"] = ""

    parent_feature_element = product.find('ul', class_='vFw0gD')
    features_list = []
    for feature in parent_feature_element.find_all('li', class_='tVe95H'):
        features_list.append(feature.text)
    product_dict["features"] = ', '.join(features_list)

    scraped_info_list.append(product_dict)
    connect.insert_into_table(tuple(product_dict.values()))

dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("laptops.csv")
connect.get_laptop_info()

'''
Output :-

Table created successfully
('Dell 14 3000 Core i3 7th Gen - (4 GB/1 TB HDD/Linux) inspiron 3481 Laptop', '4.1', '₹25,490', '13% off', 'Intel Core i3 Processor (7th Gen), 4 GB DDR4 RAM, Linux/Ubuntu Operating System, 1 TB HDD, 35.56 cm (14 inch) Display, 1 Year Limited Hardware Warranty, InHome Service After Remote Diagnosis')
('HP 14q Core i3 7th Gen - (8 GB/256 GB SSD/Windows 10 Home) 14q-cs0023TU Thin and Light Laptop', '4.3', '₹32,990', '3% off', 'Intel Core i3 Processor (7th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 256 GB SSD, 35.56 cm (14 inch) Display, 1 Year Onsite Warranty')
('Lenovo Ideapad 130 Core i3 7th Gen - (4 GB/1 TB HDD/Windows 10 Home) 130-15IKB Laptop', '4', '₹27,990', '15% off', 'Intel Core i3 Processor (7th Gen), 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('HP 15 Pentium Gold - (4 GB/1 TB HDD/Windows 10 Home) 15-di0001TU Laptop', '4.4', '₹23,490', '8% off', 'Intel Pentium Gold Processor, 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('HP 15s Ryzen 3 Dual Core - (4 GB/256 GB SSD/Windows 10 Home) 15s-eq0007AU Thin and Light Laptop', '4.5', '₹30,990', '4% off', 'AMD Ryzen 3 Dual Core Processor, 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 256 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Lenovo Ideapad L340 Core i5 9th Gen - (8 GB/1 TB HDD/128 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA G...', '4.5', '₹59,990', '39% off', '60 Hz Refresh Rate- It can display upto 60 frames per second., Intel Core i5 Processor (9th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD|128 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Acer Nitro 5 Core i7 9th Gen - (8 GB/1 TB HDD/256 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA Geforce ...', '4.6', '₹69,990', '33% off', '60 Hz Refresh Rate- It can display upto 60 frames per second., Intel Core i7 Processor (9th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD|256 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year International Travelers Warranty (ITW)')
('Dell Vostro 15 3000 Core i3 7th Gen - (4 GB/1 TB HDD/Linux) 3581 Laptop', '4.4', '₹26,490', '17% off', 'Intel Core i3 Processor (7th Gen), 4 GB DDR4 RAM, Linux/Ubuntu Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Limited Hardware Warranty, In Home Service After Remote Diagnosis - Retail')
('Asus TUF Gaming Ryzen 5 Quad Core - (8 GB/1 TB HDD/Windows 10 Home/3 GB Graphics/NVIDIA Geforce GTX 10...', '4.6', '₹46,990', '35% off', 'AMD Ryzen 5 Quad Core Processor, 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 43.94 cm (17.3 inch) Display, 1 Year Onsite Warranty')
('HP Pavilion x360 Core i3 8th Gen - (4 GB/256 GB SSD/Windows 10 Home) 14-dh0107TU 2 in 1 Laptop', '4.5', '₹42,990', '5% off', 'Intel Core i3 Processor (8th Gen), 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 256 GB SSD, 35.56 cm (14 inch) Touchscreen Display, 1 Year Onsite Warranty')
('Lenovo Ideapad S145 Ryzen 3 Dual Core - (4 GB/1 TB HDD/Windows 10 Home) S145-15API Thin and Light Lapt...', '4', '₹27,990', '10% off', 'AMD Ryzen 3 Dual Core Processor, 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466', '4.7', '₹65,990', '22% off', 'Intel Core i5 Processor (5th Gen), 8 GB DDR3 RAM, 64 bit Mac OS Operating System, 128 GB SSD, 33.78 cm (13.3 inch) Display, 1 Year Carry In Warranty')
('Lenovo Ideapad S145 Core i5 10th Gen - (8 GB/1 TB HDD/Windows 10 Home) S145-15IIL Laptop', '', '₹42,990', '31% off', 'Intel Core i5 Processor (10th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Lenovo Ideapad S145 Core i3 10th Gen - (4 GB/256 GB SSD/Windows 10 Home) S145-15IIL Thin and Light Lap...', '4.4', '₹35,490', '26% off', 'Intel Core i3 Processor (10th Gen), 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 256 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Acer Nitro 5 Ryzen 5 Quad Core - (8 GB/1 TB HDD/Windows 10 Home/4 GB Graphics/NVIDIA Geforce GTX 1650)...', '4.5', '₹52,990', '28% off', 'AMD Ryzen 5 Quad Core Processor, 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year International Travelers Warranty (ITW)')
('Apple MacBook Air Core i5 8th Gen - (8 GB/128 GB SSD/Mac OS Mojave) MVFM2HN/A', '4.7', '₹89,990', '9% off', 'Intel Core i5 Processor (8th Gen), 8 GB DDR3 RAM, Mac OS Operating System, 128 GB SSD, 33.78 cm (13.3 inch) Display, 1 Year Onsite Warranty')
('Lenovo Ideapad 130 Core i5 8th Gen - (8 GB/1 TB HDD/Windows 10 Home/2 GB Graphics) 130-15IKB Laptop', '4.1', '₹42,990', '20% off', 'Intel Core i5 Processor (8th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('HP 15q Core i5 8th Gen - (8 GB/1 TB HDD/Windows 10 Home) 15q-ds1001TU Laptop', '4.3', '₹46,990', '4% off', 'Intel Core i5 Processor (8th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Asus VivoBook Gaming Core i5 9th Gen - (8 GB + 32 GB Optane/512 GB SSD/Windows 10 Home/4 GB Graphics/N...', '4.5', '₹54,990', '31% off', '60 Hz Refresh Rate- It can display upto 60 frames per second., Intel Core i5 Processor (9th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 512 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year Limited International Hardware Warranty')
('HP Pavilion Core i5 9th Gen - (8 GB/1 TB HDD/Windows 10 Home/3 GB Graphics/NVIDIA Geforce GTX 1050) 15...', '4.2', '₹52,990', '19% off', 'Intel Core i5 Processor (9th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
('Asus Core i5 8th Gen - (4 GB/1 TB HDD/Windows 10 Home/2 GB Graphics) R540UB-DM1043T Laptop', '3.9', '₹36,990', '30% off', 'Full HD LCD Anti-glare Display, Intel Core i5 Processor (8th Gen), 4 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD, 39.62 cm (15.6 inch) Display, 1 Year Limited International Hardware Warranty')
('Acer Nitro 5 Ryzen 5 Quad Core - (8 GB/1 TB HDD/256 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA Geforc...', '4.8', '₹56,990', '33% off', 'AMD Ryzen 5 Quad Core Processor, 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD|256 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year International Travelers Warranty (ITW)')
('Asus VivoBook S Series Core i5 8th Gen - (8 GB/1 TB HDD/256 GB SSD/Windows 10 Home) S430FA-EB156T Thin...', '4.5', '₹52,990', '23% off', 'Intel Core i5 Processor (8th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 1 TB HDD|256 GB SSD, 35.56 cm (14 inch) Display, 1 Year Limited International Hardware Warranty')
('Lenovo Ideapad S340 Core i5 8th Gen - (8 GB/512 GB SSD/Windows 10 Home/2 GB Graphics) S340 Thin and Li...', '4.3', '₹56,990', '25% off', 'Intel Core i5 Processor (8th Gen), 8 GB DDR4 RAM, 64 bit Windows 10 Operating System, 512 GB SSD, 39.62 cm (15.6 inch) Display, 1 Year Onsite Warranty')
[Finished in 5.1s]

'''


