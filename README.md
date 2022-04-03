# Python Emlak Sitesi Uzerinden Veri Cekme Scripti
 
### Proje Amaci;
 **Excel dropdownlari ile verilen filtreler araciligi ile ( il, konut tipi vs. ) excel makrolari ile cagirilan Python dosyalari, MySQLite Veritabanina tum sayfalarda ki her ilanlarin bilgisini kayit eder.**


#### Gerekli teknojiler ;

	 Selenium, BeautifulSoup, Openpyxl, Xlsxwriter

#### Kullanmadan once ;

-Excel ayarlarindan gelisitirici arayuzunu aciktiktan sonra  **.xlsm ** uzantili excel dosyasini acip makro ayarlamalarindan scriptlerin lokasyonunu kendi cihaziniza gore girmeniz gerekiyor. ( ilanVeVeritabani.py konumu , FiltreleriCek konumu ve python.exe konumu )

-Python'u yükledikten sonra terminali yönetici olarak çalıştırın ve indirdiğiniz klasörün içerisinde kodu çalıştırın ;

	pip3 install -r requirements.txt


### Not :
Excel kullanmadan da Python dosyasini calistirarak gerekli ilanlari veri tabanina kayit ettirebilirsiniz, bunun icin hafif seviyede MySQLite ve selenium bilgisi yeterli olacaktir.
