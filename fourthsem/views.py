from django.http import HttpResponse
from django.shortcuts import render

PRODUCTS = {
    'iphone': {
        'name': 'Iphone',
        'image': '/static/iphone_new.jpg',
        'short': 'Experience the power of Apple\'s latest smartphone.',
        'price': '₹999',
        'description': 'The latest iPhone features a stunning Super Retina XDR display, A17 Pro chip for lightning-fast performance, an advanced camera system with 48MP main camera, and all-day battery life. Built with titanium design and USB-C connectivity.',
        'features': ['6.7 inch Super Retina XDR Display', 'A17 Pro Chip', '48MP Camera System', 'Titanium Design', 'USB-C Connector', 'All-Day Battery Life'],
    },
    'macbook': {
        'name': 'Macbook',
        'image': '/static/macbook_new.jpg',
        'short': 'Powerful performance for professionals and creators.',
        'price': '₹1,299',
        'description': 'MacBook Pro delivers exceptional performance with Apple M3 chip, up to 22 hours of battery life, a stunning Liquid Retina XDR display, and a premium all-aluminum unibody design. Perfect for developers, designers, and creators.',
        'features': ['Apple M3 Chip', 'Up to 22 Hours Battery', 'Liquid Retina XDR Display', '16GB Unified Memory', '512GB SSD Storage', 'MagSafe Charging'],
    },
    'accessories': {
        'name': 'Accessories',
        'image': '/static/accessories_new.jpg',
        'short': 'Complete your setup with premium accessories.',
        'price': '₹49 - ₹549',
        'description': 'Discover a wide range of Apple accessories including AirPods Pro, Apple Watch, Magic Keyboard, Magic Mouse, and more. Designed to work seamlessly with all your Apple devices.',
        'features': ['AirPods Pro', 'Apple Watch Ultra', 'Magic Keyboard', 'Magic Mouse', 'MagSafe Charger', 'Apple Pencil Pro'],
    },
    'ipad': {
        'name': 'iPad',
        'image': '/static/ipad.jpg',
        'short': 'Your next computer is not a computer.',
        'price': '₹44,900',
        'description': 'iPad Pro features the powerful M2 chip, a stunning Liquid Retina XDR display, superfast Wi-Fi 6E, and 5G connectivity. With Apple Pencil hover and ProRes video, it is the ultimate iPad experience for creative professionals.',
        'features': ['M2 Chip', '12.9 inch Liquid Retina XDR Display', 'Apple Pencil Hover', 'ProRes Video', 'Wi-Fi 6E', 'Thunderbolt / USB 4'],
    },
    'applewatch': {
        'name': 'Apple Watch',
        'image': '/static/applewatch.jpg',
        'short': 'The ultimate health and fitness companion.',
        'price': '₹44,900',
        'description': 'Apple Watch Ultra 2 features the brightest Apple display ever, precision dual-frequency GPS, up to 72 hours of battery life, and advanced health sensors. Built for endurance, exploration, and adventure.',
        'features': ['S9 SiP Chip', '3000 nits Brightness', 'Precision Dual-Frequency GPS', '72 Hour Battery Life', 'Water Resistant 100m', 'Blood Oxygen & ECG'],
    },
    'airpods': {
        'name': 'AirPods',
        'image': '/static/airpods.jpg',
        'short': 'Immersive sound with active noise cancellation.',
        'price': '₹24,900',
        'description': 'AirPods Pro 2nd generation deliver up to 2x more Active Noise Cancellation, Adaptive Transparency, and Personalized Spatial Audio. With the H2 chip, they offer richer sound and a more immersive listening experience.',
        'features': ['H2 Chip', 'Active Noise Cancellation', 'Adaptive Transparency', 'Personalized Spatial Audio', 'Up to 6 Hours Listening', 'MagSafe Charging Case'],
    },
    'appletv': {
        'name': 'Apple TV',
        'image': '/static/appletv.jpg',
        'short': 'Cinema-level experience in your living room.',
        'price': '₹14,900',
        'description': 'Apple TV 4K brings the best of cinema home with Dolby Vision, Dolby Atmos, and HDR10+. Powered by the A15 Bionic chip, it delivers fast performance and supports all your favorite streaming services.',
        'features': ['A15 Bionic Chip', '4K HDR Dolby Vision', 'Dolby Atmos Sound', 'Siri Remote', 'AirPlay & SharePlay', '128GB Storage'],
    },
}

def homepage(request):
    data={
        'number':[-1,1,2,3,4,5],
        'products': PRODUCTS,
        }
    return render(request,"Index.html",data)

def product_detail(request, product_name):
    product = PRODUCTS.get(product_name)
    if product:
        return render(request, "product_detail.html", {'product': product})
    return HttpResponse("<h1>Product not found</h1>")

def aboutUS(request):
    return HttpResponse("<h1>Welcome to Department of computer science....</h1>")

def course(request):
    return HttpResponse("<h1>we have this couurses....</h1>")

def courseDetails(request,courseid):
    return HttpResponse(courseid,"<h1>How are you...</h1>")

def courseDetails1(request,coursename):
    return HttpResponse(coursename+"<h1>Hiii,MAJAMA</h1>")

def courseDetails2(request,courseslug):
    return HttpResponse(courseslug + "<h1>How are you......</h1>")


