# random_image_viewer

handleiding
1. pipenv installeren op terminal (zie jetbrains handleiding):
   1. open terminal (cmd prompt)
   2. _installeer pip_
   3. pip install --user pipenv
2. pipenv aan pad toevoegen
   1. vind pad van python scripts door "py -m site --user-site"
   2. zet path: "$ setx PATH "%PATH%;C:\Users\YOURNAME\AppData\Roaming\Python\PYTHONVERSION\Scripts" "
   
3. project clonen met git
4. django installeren
   1. PYTHON terminal: pip install django
5. python manage.py runserver
   1. duurt een halfuur: via sparql alle manifesten ophalen en bewaren in dataframe
   2. _beter om direct in csv te bewaren_  (+ manier nodig om alle unieke rijen te filteren, of enkel unieke manifesten toe te voegen tijdens de query. manifestenDMG heeft 140.000+ rijen voor 3000 objectnummers > onhandelbaar groot)
6. open http://127.0.0.1:8000/getimage/image/
7. herlaad voor een nieuw willekeurig beeld

aanpassingen?
- image.html > tekst of velden
- styles.css > kleuren en stijl
  - bij aanpassingen in styles > pagina volledig herladen door ctrl+f5
- views.py > welke info uit manifest halen en tonen
- 
