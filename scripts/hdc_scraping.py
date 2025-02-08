import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

def scraping(indicator='indicator', url='url', level='level', yearback=5):
    
    # Set download path to current folder
    options = Options()
    base_download_dir = os.path.abspath(f"downloads/{level}") # Change the path if you need
    options.add_experimental_option('prefs', {
        'download.default_directory': base_download_dir
    })

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)

    # === Scraping ===    
    indicator_folder = os.path.join(base_download_dir, indicator)
    os.makedirs(indicator_folder, exist_ok=True)

    print(f"Extracting {indicator}: {url}")  # Optional logging
    driver.get(url)

    # change to old interface 
    old_report_button = driver.find_element(By.XPATH, "//span[@onclick='seeReportOld()']")
    old_report_button.click()

    # Wait for the table to load (about 20 seconds)
    wait = WebDriverWait(driver, timeout=60)
    wait.until(lambda d: driver.find_element(By.ID, 'ptable').is_displayed())

    # Select the level of extraction
    type = Select(driver.find_element(By.ID, 'selSP'))
    area = Select(driver.find_element(By.ID, 'selAllProv'))
    sel_year = Select(driver.find_element(By.ID, 'selYear'))
    sel_zone = Select(driver.find_element(By.ID, 'selZone'))
    
    for y_option in sel_year.options[:yearback]: # change number to download from last N year
        
        year = y_option.text
        sel_year.select_by_visible_text(year)
        
        year_folder = os.path.join(indicator_folder, year)
        os.makedirs(year_folder, exist_ok=True)
        
        if level in ['รายอำเภอ']:
            
            if level == 'รายเขตสุขภาพ':
                type.select_by_visible_text('เขตพื้นที่')
                area.select_by_visible_text('เขตสุขภาพ')
                sel_zone.select_by_visible_text('------- ทั้งหมด ------')
                
                attempts = 0
                success = False
                
            elif level == 'รายอำเภอ':
                type.select_by_visible_text('เขตพื้นที่')
                area.select_by_visible_text('รายอำเภอ')
                
                
                for z_option in sel_zone.options[1:]:  # Skip the first "------ ทั้งหมด ------" option
                    zone_name = z_option.text
                    print(zone_name)
                    # Select zone
                    sel_zone.select_by_visible_text(z_option.text)
                    
                    attempts = 0
                    success = False
                    
                    while attempts < 3 and not success:  # Retry 3 times
                        try:
                            # Click ok button 
                            driver.find_element(By.ID, 'btnOkey').click()
                            wait.until(lambda d: d.find_element(By.ID, 'ptable').is_displayed())
                
                            # Download the data
                            driver.execute_script(f"$('#dataTable').tableExport({{type:'csv',escape:false,tableName:'{indicator}_{z_option.text}_{year}'}});")
                            time.sleep(3)
                            shutil.move(os.path.join(base_download_dir, f'{indicator}_{z_option.text}_{year}.csv'), os.path.join(year_folder, f'{indicator}_{z_option.text}_{year}.csv'))
                            print('done')
                            success = True  # exit the retry loop
                        except Exception as e:
                            print(f"Error: {e}")
                            print("Retrying")
                            attempts += 1  
                            if attempts == 3:  # If still fails, proceed to next province
                                print("Max retries")
                                success = True
                        except Exception as e:
                            print(f"Error: {e}")
                            print(f"Retrying")
                            attempts += 1
                            if attempts == 3:  # If still fails, proceed to next province
                                success = True
                    
        else:
            print("Please select the level for extraction from'เขตพื้นที่', 'Service Plan', 'รายโรงพยาบาล', 'รายหน่วยบริการ', 'เครือข่ายบริการ'")




    # sel_year = Select(driver.find_element(By.ID, 'selYear'))

    # # Select the last 5 years from the dropdown
    # for y_option in sel_year.options[:5]: # change number to download from last N year
    #     year = y_option.text
    #     print(f'year: {year}')
    #     sel_year.select_by_visible_text(year) 

    #     year_folder = os.path.join(indicator_folder, year)
    #     os.makedirs(year_folder, exist_ok=True)

    #     try:
    #         sel_month = Select(driver.find_element(By.ID, 'selMonth'))
    #         sel_month.select_by_visible_text('ธันวาคม')  # <- Change report month here
    #     except:
    #         print("Dropdown not found, continuing script...")

    #     #  รายอำเภอ 
    #     sel_month = Select(driver.find_element(By.ID, 'selAllProv'))
    #     sel_month.select_by_visible_text('รายอำเภอ') 

    #     # เขต
    #     sel_zone = Select(driver.find_element(By.ID, 'selZone'))
    #     for z_option in sel_zone.options[1:]:  # Skip the first "------ ทั้งหมด ------" option
    #         zone_name = z_option.text
    #         # Select zone
    #         sel_zone.select_by_visible_text(z_option.text)

    #         attempts = 0
    #         success = False

    #         while attempts < 3 and not success:  # Retry 3 times
    #             try:
    #                 # Click ok button 
    #                 driver.find_element(By.ID, 'btnOkey').click()
    #                 wait.until(lambda d: d.find_element(By.ID, 'ptable').is_displayed())
        
    #                 # Download the data
    #                 driver.execute_script(f"$('#dataTable').tableExport({{type:'csv',escape:false,tableName:'{indicator}_{z_option.text}_{year}'}});")
    #                 time.sleep(3)
    #                 shutil.move(os.path.join('data/indicators', f'{indicator}_{z_option.text}_{year}.csv'), os.path.join(year_folder, f'{indicator}_{z_option.text}_{year}.csv'))
    #                 print('done')
    #                 success = True  # exit the retry loop
    #             except Exception as e:
    #                 print(f"Error: {e}")
    #                 print("Retrying")
    #                 attempts += 1  
    #                 if attempts == 3:  # If still fails, proceed to next province
    #                     print("Max retries")
    #                     success = True
    #             except Exception as e:
    #                 print(f"Error: {e}")
    #                 print(f"Retrying")
    #                 attempts += 1
    #                 if attempts == 3:  # If still fails, proceed to next province
    #                     success = True
            
    # print(f'Finising scraped for {indicator} ==========')