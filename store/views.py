from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Categories,Products
from django.urls import reverse
from django.contrib import messages

import csv
# Create your views here.

categories = ['WoowZerz', 'La Bele', 'Stylo Bug', 'Alom', 'Label Ritu Kumar', 'Jompers', 'SWHF', 'Dennis Morton', 'Rajesh Silk Mills', 'RAJUBHAI HARGOVINDAS', 'akavya', 'TATTVA', 'La Zoire', 'Raymond Home', 'Shree', 'Blissta', 'Gatha', 'Arch Elements', 'Cottinfab', 'SG LEMAN', 'Clovia', 'RAISIN', 'Saree mall', 'Kuons Avenue', 'Saadgi', 'Shree Shubh', 'mf', 'TREEMODA', 'Jansons', 'PAROKSH', 'Kidling', 'Chitwan Mohan', 'Boutique Living India', 'Mirage', 'Manyavar', 'Peter England', 'SCOUP', 'Sanwara', 'WESTCLO', 'Louis Park', 'Colour Me by Melange', 'Ethnicity', 'PIZUNA LINENS', 'Rodamo', 'Independence Club', 'Dreamscape', 'Twisha', 'Lombard', 'Raas', 'My Little Lambs', 'pspeaches', 'Athena', 'MOHANLAL SONS', 'Very Me', 'Larwa', 'AKS Couture', 'MAFATLAL', 'TALES & STORIES', 'BOMBAY DYEING', 'SOHO By MAFATLAL', 'all about you', "Kurti's by Menka", 'Sringam', 'Kira Plus', 'Indibelle', 'IVOC', 'Story@home', 'SOJANYA', 'BIANCA', 'Trend Arrest', 'KISAH', 'Blue Saint', '20Dresses', 'Cortina', 'The Magic Wand', 'Breakbounce', 'Chennis', 'pinkshink', 'WEAVERS VILLA', 'Crafts collection', 'Prayyan', 'Indian Attire', 'HERE&NOW', 'Tulsattva', 'I AM FOR YOU', 'Aksara', 'K&U', 'SOUNDARYA', 'Jack & Jones', 'VASTRAMAY', 'L.A. SEVEN', 'Rangriti', 'Home Sizzler', 'Citypret', 'aasi', 'Svanik', 'Ishin', 'Naari', 'Vishudh', 'A Little Fable', 'Aj DEZInES', 'Be Indi', 'IndusDiva Loomnic', 'Styles Closet', 'UNTUNG', 'MASPAR', 'AASI - HOUSE OF NAYO', 'Anouk', 'House This', 'Dupatta Bazaar', 'Routeen', 'Zotw', 'CORE Designed by SPACES', 'anayna', 'indus route by Pantaloons', 'TAG 7', 'MARK HOME', 'SEJ by Nisha Gupta', 'V SALES', 'Sanjhi', 'JADE BLUE', 'Freehand', 'Ritu Kumar', 'SYONN', 'House of Pataudi', 'Terry Fator', 'Trident', 'INDYA', 'Nature Casuals', 'Vivids India', 'BownBee', 'Hypernation', 'Ethnix by Raymond', 'Shaily', 'ADIVA', 'Campana', 'Tiber Taber', 'shiloh', 'MABISH by Sonal Jain', 'Jeetethnics', 'Myshka', 'British Club', 'PANIT', 'Aasvaa', 'ROMEE', 'Nick&Jess', 'MR BUTTON', 'Abhishti', 'JAINISH', 'Aujjessa', 'Portico New York', 'I Know', 'ROYAL KURTA', 'Huesland', 'The Indian Garage Co', 'KAANCHIE NANGGIA', 'AURELIA', 'Khoday Williams', 'KID1', 'Varanga', 'Anekaant', 'rangeelo rajasthan', 'breya', 'Nayo', 'BLUSH', 'Yellow Kite', 'Laabha', 'CHOKORE', 'RG DESIGNERS', 'Azira', 'Rajasthan Decor', 'W', 'AKS', 'Alina decor', 'RARE ROOTS', 'Divine Casa', 'PIVOTO', 'Pluchi', 'Bollywood Vogue', 'Jaipur Kurti', 'Manu', 'EverHOME', 'Juniper', 'Chhabra 555', 'STELLAR HOME', 'Kira', 'Satrani', 'RIKIDOOS', 'CHRISTY', 'TOZZI', 'Wintage', 'Style Quotient', 'Fairies Forever', 'Biba', 'SHOWOFF', 'TJORI', 'SG YUVRAJ', 'SPACES', 'Celio', 'IMARA', 'Libas', 'DEYANN', 'Dazzio', 'Shakumbhari', 'RIYA', 'Yufta', 'Taavi', 'studio rasa', 'Bitterlime', 'A Homes Grace', 'LilPicks', 'Pantaloons Junior', 'Bene Kleed', 'La Firangi', 'THE SILHOUETTE STORE', 'STREET 9', '612 league', 'Globus', 'Peaches', 'RANGMANCH BY PANTALOONS', 'Hangup', 'Fabindia', 'Ira Soleil', 'Peter England Casuals', 'Yuris', 'Rohit Bal Limited', 'irin', 'Purple State', 'Faballey Indya', 'PINKSKY', 'Salona Bichona', 'Abhiyuthan', 'SWAYAM', 'Clora Creation', 'URBAN DREAM', 'Home Ecstasy', 'WONDERMOM', 'Raymond Ethnix', 'Aarika', 'Manish Creations', 'VULCAN', 'NEUDIS', 'Noi', 'Castle', 'AKKRITI BY PANTALOONS', 'Shaftesbury London', 'LUXURAZI', 'Gini and Jony', 'PITARA', 'Fuzion Couture', 'See Designs', 'TABARD', 'U.S. Polo Assn. Kids', 'AgrohA', 'The White Willow', 'DDecor', 'Moda Rapido', 'Melange by Lifestyle', 'United Colors of Benetton', 'LOCOMOTIVE', 'Ahmedabad Cotton', 'GMF', 'Solemio', 'Banarasi Style', 'Soch', 'ANAISA', 'SASSAFRAS', 'Drama Sisters', 'Toshee', 'Sangria', 'Mangalyam British Club', 'Global Desi', 'GERUA', 'Indo Era', 'Aura', 'Inddus', 'Faserz', 'Rajyog', 'JBN Creation', 'Bitiya by Bhama', 'A.T.U.N All Things Uber Nice', 'Fusion Beats', 'SUTRAM', 'Silk India', 'Indian Poshakh', 'Nation Polo Club', 'even', 'Imfashini', 'Stylee LIFESTYLE', 'Amora', 'Ayaany', 'SALWAR STUDIO', 'CHILL WINSTON', 'BETTY', 'Hubberholme', 'YK', 'Cross Court', 'Geroo Jaipur']


def home(request):
    trending_products=Products.objects.filter(trending=1)
    category=Categories.objects.filter(status=0)
    context={'trending_products':trending_products,'category':category}
    return render(request,'index.html',context)


def collections(request):
    category=Categories.objects.filter(status=0)
    context={'category':category}
    return render(request, 'collections.html',context)


def collectionsView(request,slug):
    if Categories.objects.filter(slug=slug,status=0).exists():
        products=Products.objects.filter(category__slug=slug)
        category=Categories.objects.get(slug=slug)
        context={"products":products,"category":category};
        return render(request, 'products/index.html',context)
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))


def productView(request,cate_slug,pro_slug):
    if Categories.objects.filter(slug=cate_slug,status=0).exists():
        if Products.objects.filter(slug=pro_slug,status=0).exists():
            products=Products.objects.get(slug=pro_slug,status=0)
            context={"products":products}
            return render(request, 'products/view.html',context)
        else:
            messages.error(request,"No such product found");
            return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))
