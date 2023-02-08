$path = 'C:\Users\Baachus\Desktop\Files\Automation\Playwright - Example\Tests'
$file = '\Bing\bing_test.py'

$cmd = $path+"\\"+$file  # This line of code will create the concatenate the path and file
Start-Process $cmd  # This line will execute the cmd 