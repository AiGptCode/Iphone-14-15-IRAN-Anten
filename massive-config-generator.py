ab70249a-44de-4dd3-b5bb-c6be267e68a7
#ابتداکد شبکه ها که شخصی سازس کردید جایگیزین کنید 
# کدهای شبکه
‏network_configs = {
‏    "All Network": {
        # تنظیمات کانفیگ All Network اینجا وارد شوند
    },
‏    "Hamrah Aval": {
        # تنظیمات کانفیگ Hamrah Aval اینجا وارد شوند
    },
‏    "Irancel": {
        # تنظیمات کانفیگ Irancel اینجا وارد شوند
    },
‏    "Rightel": {
        # تنظیمات کانفیگ Rightel اینجا وارد شوند
    },
}

# انتخاب کانفیگ
‏print("لطفاً یک کانفیگ را انتخاب کنید:")
‏for index, config_name in enumerate(network_configs.keys(), start=1):
‏    print(f"{index}. {config_name}")

‏selected_index = int(input("شماره کانفیگ مورد نظر خود را وارد کنید: "))
‏selected_config_name = list(network_configs.keys())[selected_index - 1]
‏selected_config = network_configs[selected_config_name]

# تنظیمات پروکسی
‏need_proxy = input("آیا نیاز به تنظیمات پروکسی دارید؟ (بله/خیر): ").strip().lower()
‏if need_proxy == "بله":
‏    proxy_server = input("لطفاً آدرس سرور پروکسی را وارد کنید: ")
‏    proxy_port = int(input("لطفاً پورت پروکسی را وارد کنید: ")
‏else:
‏    proxy_server = ""
‏    proxy_port = 0

# ایجاد شناسه‌های یکتا با استفاده از کتابخانه uuid
‏unique_ids = [str(uuid.uuid4()) for _ in range(5)]  # می‌توانید تعداد شناسه‌ها را تغییر دهید

# اضافه کردن شناسه‌های یکتا به کانفیگ
‏selected_config["UniqueIDs"] = unique_ids

# اضافه کردن تنظیمات پروکسی اگر نیاز باشد
‏if need_proxy == "بله":
‏    selected_config["ProxyServer"] = proxy_server
‏    selected_config["ProxyPort"] = proxy_port

# نمایش کانفیگ نهایی
‏print("\nکانفیگ نهایی:")
‏print(selected_config)
