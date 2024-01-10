from action import dim_install, install_opendata, download_comparison_folder, read_existing_data, read_current_data, show_data_diff, update_data
'''
import schedule
import time
'''

# Install OTTOP open data

dim_install()

'''
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472131","うるま市")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003002626","とかしき観光バス合同会社")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9340001004024","マリックスライン株式会社")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5340001010554","マルエーフェリー株式会社")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7000020473821","与那国町")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473286","中城村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360001012745","中央交通（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360001000835","久米商船（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473618","久米島町")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360003002575","久高海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9000020473596","伊平屋村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473600","伊是名村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360001012407","伊江島観光バス（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473154","伊江村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360001013190","八重山観光フェリー（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473278","北中城村")

install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/3000020472158","南城市")

install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003007856","合同会社やんばる急行バス")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360003005178","合名会社大神海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1000020472093","名護市")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473014","国頭村役場")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473758","多良間村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360003005256","多良間海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360003005301","宮古協栄バス（資）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360001007585","平安座総合開発（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473545","座間味村役場")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/3360002008754","有限会社カリー観光")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360001013023","東バス")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7011501003070","東京バス株式会社")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473031","東村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001015810","東陽バス（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/8360003004772","水納海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/360005005779","沖縄エアポートシャトルLLP")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001000457","沖縄バス（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472115","沖縄市")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360001000447","沖縄都市モノレール株式会社")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473537","渡嘉敷村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360001013238","由布島")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5360003005096","福山海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5290801024676","第一マリンサービス")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473553","粟国村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472107","糸満市")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360002020959","船浮海運")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001013046","西表島交通（株）")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7000020473243","読谷村")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360002020964","（有）安栄観光")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360002013009","（有）神谷観光")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360002021665","（有）竹富島交通")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5360001014132","（株）八千代バス・タクシー")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360003005217","（資）共和バス")
install_opendata("https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003005018","（資）浦内川観光")
'''

# Specify the URL, destination directory, and folder name of the folder to download
folder_list = [
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472131", "name": "うるま市"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003002626", "name": "とかしき観光バス合同会社"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9340001004024", "name": "マリックスライン株式会社"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5340001010554", "name": "マルエーフェリー株式会社"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7000020473821", "name": "与那国町"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473286", "name": "中城村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360001012745", "name": "中央交通（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360001000835", "name": "久米商船（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473618", "name": "久米島町"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360003002575", "name": "久高海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9000020473596", "name": "伊平屋村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473600", "name": "伊是名村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360001012407", "name": "伊江島観光バス（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473154", "name": "伊江村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360001013190", "name": "八重山観光フェリー（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473278", "name": "北中城村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/3000020472158", "name": "南城市"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003007856", "name": "合同会社やんばる急行バス"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360003005178", "name": "合名会社大神海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1000020472093", "name": "名護市"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020473014", "name": "国頭村役場"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473758", "name": "多良間村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360003005256", "name": "多良間海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7360003005301", "name": "宮古協栄バス（資）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360001007585", "name": "平安座総合開発（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473545", "name": "座間味村役場"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/3360002008754", "name": "有限会社カリー観光"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360001013023", "name": "東バス"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7011501003070", "name": "東京バス株式会社"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4000020473031", "name": "東村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001015810", "name": "東陽バス（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/8360003004772", "name": "水納海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/360005005779", "name": "沖縄エアポートシャトルLLP"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001000457", "name": "沖縄バス（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472115", "name": "沖縄市"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360001000447", "name": "沖縄都市モノレール株式会社"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473537", "name": "渡嘉敷村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360001013238", "name": "由布島"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5360003005096", "name": "福山海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5290801024676", "name": "第一マリンサービス"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2000020473553", "name": "粟国村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5000020472107", "name": "糸満市"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360002020959", "name": "船浮海運"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/2360001013046", "name": "西表島交通（株）"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/7000020473243", "name": "読谷村"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360002020964", "name": "（有）安栄観光"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/6360002013009", "name": "（有）神谷観光"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/4360002021665", "name": "（有）竹富島交通"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/5360001014132", "name": "（株）八千代バス・タクシー"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/9360003005217", "name": "（資）共和バス"},
    {"url": "https://api3.ottop.org/download/gtfs/ooXuXei4op7y/1360003005018", "name": "（資）浦内川観光"},
]
save_folder = "./temporary_file"


# Download and extract each folder
for folder in folder_list:
    download_comparison_folder(folder["url"], save_folder, folder["name"])


# Show data difference
existing_data = read_existing_data("./data_files/")
current_data, file_names = read_current_data("./temporary_file/")
show_data_diff(file_names, existing_data, current_data)

'''
# Scheduled execution every hour
def job():
    print("Running the job...")
    existing_data = read_existing_data("./data_files/")
    current_data, file_names = read_current_data("./temporary_file/")
    show_data_diff(file_names, existing_data, current_data)

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''

# Update opendata
update_data()
