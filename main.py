import bs4
import requests
from bs4 import BeautifulSoup

class ProjectSpider(scrapy.Spider):
   name = "main"

   html = """
<select name="ctl00$ContentPlaceHolder1$ddlCounty" onchange="javascript:setTimeout(&#39;__doPostBack(\&#39;ctl00$ContentPlaceHolder1$ddlCounty\&#39;,\&#39;\&#39;)&#39;, 0)" id="ContentPlaceHolder1_ddlCounty" class="form-control">
		<option selected="selected" value="-Select County-">-Select County-</option>
		<option value="000">ADAIR</option>
		<option value="010">ANDREW</option>
		<option value="020">ATCHISON</option>
		<option value="030">AUDRAIN</option>
		<option value="040">BARRY</option>
		<option value="050">BARTON</option>
		<option value="060">BATES</option>
		<option value="070">BENTON</option>
		<option value="080">BOLLINGER</option>
		<option value="090">BOONE</option>
		<option value="100">BUCHANAN</option>
		<option value="110">BUTLER</option>
		<option value="120">CALDWELL</option>
		<option value="130">CALLAWAY</option>
		<option value="140">CAMDEN</option>
		<option value="150">CAPE GIRARDEAU</option>
		<option value="160">CARROLL</option>
		<option value="170">CARTER</option>
		<option value="180">CASS</option>
		<option value="190">CEDAR</option>
		<option value="200">CHARITON</option>
		<option value="210">CHRISTIAN</option>
		<option value="220">CLARK</option>
		<option value="230">CLAY</option>
		<option value="240">CLINTON</option>
		<option value="250">COLE</option>
		<option value="260">COOPER</option>
		<option value="270">CRAWFORD</option>
		<option value="280">DADE</option>
		<option value="290">DALLAS</option>
		<option value="300">DAVIESS</option>
		<option value="310">DEKALB</option>
		<option value="320">DENT</option>
		<option value="330">DOUGLAS</option>
		<option value="340">DUNKLIN</option>
		<option value="350">FRANKLIN</option>
		<option value="360">GASCONADE</option>
		<option value="370">GENTRY</option>
		<option value="380">GREENE</option>
		<option value="390">GRUNDY</option>
		<option value="400">HARRISON</option>
		<option value="410">HENRY</option>
		<option value="411">HICKORY</option>
		<option value="412">HOLT</option>
		<option value="440">HOWARD</option>
		<option value="450">HOWELL</option>
		<option value="460">IRON</option>
		<option value="470">JACKSON</option>
		<option value="480">JASPER</option>
		<option value="490">JEFFERSON</option>
		<option value="500">JOHNSON</option>
		<option value="510">KNOX</option>
		<option value="520">LACLEDE</option>
		<option value="530">LAFAYETTE</option>
		<option value="540">LAWRENCE</option>
		<option value="541">LEWIS</option>
		<option value="560">LINCOLN</option>
		<option value="570">LINN</option>
		<option value="580">LIVINGSTON</option>
		<option value="600">MACON</option>
		<option value="601">MADISON</option>
		<option value="620">MARIES</option>
		<option value="630">MARION</option>
		<option value="590">MCDONALD</option>
		<option value="631">MERCER</option>
		<option value="650">MILLER</option>
		<option value="660">MISSISSIPPI</option>
		<option value="670">MONITEAU</option>
		<option value="680">MONROE</option>
		<option value="690">MONTGOMERY</option>
		<option value="700">MORGAN</option>
		<option value="710">NEW MADRID</option>
		<option value="720">NEWTON</option>
		<option value="730">NODAWAY</option>
		<option value="740">OREGON</option>
		<option value="750">OSAGE</option>
		<option value="751">OZARK</option>
		<option value="770">PEMISCOT</option>
		<option value="780">PERRY</option>
		<option value="790">PETTIS</option>
		<option value="800">PHELPS</option>
		<option value="810">PIKE</option>
		<option value="820">PLATTE</option>
		<option value="821">POLK</option>
		<option value="840">PULASKI</option>
		<option value="850">PUTNAM</option>
		<option value="860">RALLS</option>
		<option value="870">RANDOLPH</option>
		<option value="880">RAY</option>
		<option value="881">REYNOLDS</option>
		<option value="900">RIPLEY</option>
		<option value="910">SAINT CHARLES</option>
		<option value="911">SAINT CLAIR</option>
		<option value="930">SAINT FRANCOIS</option>
		<option value="940">SAINT LOUIS</option>
		<option value="950">SAINT LOUIS CITY</option>
		<option value="960">SAINTE GENEVIEVE</option>
		<option value="970">SALINE</option>
		<option value="980">SCHUYLER</option>
		<option value="981">SCOTLAND</option>
		<option value="982">SCOTT</option>
		<option value="983">SHANNON</option>
		<option value="984">SHELBY</option>
		<option value="985">STODDARD</option>
		<option value="986">STONE</option>
		<option value="987">SULLIVAN</option>
		<option value="988">TANEY</option>
		<option value="989">TEXAS</option>
		<option value="990">VERNON</option>
		<option value="991">WARREN</option>
		<option value="992">WASHINGTON</option>   
		<option value="993">WAYNE</option>
		<option value="994">WEBSTER</option>
		<option value="995">WORTH</option>
		<option value="996">WRIGHT</option>

	</select>

"""

  selectors = ["Select$0","Select$1","Select$2","Select$3","Select$4","Select$5","Select$6","Select$7","Select$8","Select$9","Select$10", "Select$11","Select$12","Select$13","Select$14","Select$15"]

   soup = BeautifulSoup(html,"lxml")

   items = soup.select('option[value]')
   values = [item.get('value') for item in items]
   textvalues = [item.text for item in items]


   def start_requests(self):
       url = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx',]


       for i in values
          for j in selectors
             def parse(self, response):
                if response.status == 200:
                   facility_name = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_FacilityName_0"]').extract_first()
	           administrator = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_Label2_0"]').extract_first()
                   address       = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lblAddress_0"]').extract_first()
                   phone_number  = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lblPhoneNumber_0"]').extract_first()
                   operator      = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lbloperator_0"]').extract_first()
                   total_number_licensed_beds = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lblTotalLicensedBeds_0"]').extract_first()
                   medicare_beds = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicareBeds_0"]').extract_first()
                   medicaid_beds = response.xpath('//span [@id = "ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicaidBeds_0"]').extract_first()

               else:
                   break
      
