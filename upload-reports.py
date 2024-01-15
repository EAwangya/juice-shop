import requests
import sys

def import_scan(file_name, scan_type):
    url = 'https://demo.defectdojo.org/api/v2/import-scan/'
    headers = {'Authorization': 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'}
    data = {
        'active': True,
        'verified': True,
        'scan_type': scan_type,
        'minimun_severity': 'Low',
        'engagement': 26
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
    elif file_name == 'retire.json':
        scan_type = 'Retire.js Scan'
    elif file_name == 'trivy.json':
        scan_type = 'Trivy Scan'
    else:
        print(f'Unsupported scan file: {file_name}')
        sys.exit(1)

    import_scan(file_name, scan_type)

if __name__ == "__main__":
    main()
