import requests
import sys

def import_scan(file_name, scan_type):
    url = 'https://demo.defectdojo.org/api/v2/import-scan/'
    headers = {'Authorization': 'Token 98127ac75ed0db3fe4185a42f822fc214e404ed9'}
    data = {
        'active': True,
        'verified': True,
        'scan_type': scan_type,
        'minimun_severity': 'Low',
        'engagement': 23
    }

    files = {'file': open(file_name, 'rb')}
    response = requests.post(url, headers=headers, data=data, files=files) 

    if response.status_code == 201:
        print(f'{scan_type} scan results imported successfully')
    else:
        print(f'Failed to import {scan_type} scan results: {response.content}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 your_script.py <scan_file>')
        sys.exit(1)

    file_name = sys.argv[1]
    scan_type = ''

    if file_name == 'gitleaks_scan.json':
        scan_type = 'Gitleaks Scan'
    elif file_name == 'njs_scan.sarif':
        scan_type = 'SARIF' 
    elif file_name == 'semgrep_scan.json':
        scan_type = 'Semgrep JSON Report'
    elif file_name == 'retirejs_scan.json':
        scan_type = 'Retire.js Scan'
    elif file_name == 'dependency-check-report.xml':
        scan_type = 'Dependency Check Scan'
    elif file_name == 'trivy.json':
        scan_type = 'Trivy Scan'
    else:
        print(f'Unsupported scan file: {file_name}')
        sys.exit(1)

    import_scan(file_name, scan_type)

if __name__ == "__main__":
    main()
