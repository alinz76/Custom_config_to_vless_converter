import json
import urllib.parse
import random


# The JSON configuration as a string
with open('__path to data.json file__') as file:
    configs = json.load(file)

country_codes = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']


# Generating random flags
def flag(country_code):
    return chr(127397 + ord(country_code[0])) + chr(127397 + ord(country_code[1]))


# Convert the JSON string to a dictionary
for config_dict in configs:
    vless_config = next((outbound for outbound in config_dict['outbounds'] if outbound['protocol'] == 'vless'), None)
    if vless_config:
        user_info = vless_config['settings']['vnext'][0]['users'][0]
        address = vless_config['settings']['vnext'][0]['address']
        port = vless_config['settings']['vnext'][0]['port']
        stream_settings = vless_config['streamSettings']
        ws_path = stream_settings['wsSettings']['path'] if 'wsSettings' in stream_settings else ''
        security = stream_settings['security']
        encryption = user_info['encryption']
        alpn = ','.join(stream_settings['tlsSettings']['alpn']) if 'tlsSettings' in stream_settings else ''
        fp = stream_settings['tlsSettings']['fingerprint'] if 'tlsSettings' in stream_settings else ''
        Type = stream_settings['network']
        sni = stream_settings['wsSettings']['headers']['Host'] if 'tlsSettings' in stream_settings else ''
        host = stream_settings['tlsSettings']['serverName'] if 'tlsSettings' in stream_settings else ''

        # Naming configs started with 'Alinz76' + random flags emoji
        config_name = "Alinz76"+flag((random.choice(country_codes)))

        # Construct the VLESS URL
        vless_url = f"vless://{user_info['id']}@{address}:{port}?path={urllib.parse.quote(ws_path)}&security={security}&encryption={encryption}&alpn={alpn}&host={host}&fp={fp}&type={Type}&sni={sni}#{config_name}"

        print(vless_url)
    else:
        print("No VLESS configuration found in the provided JSON file.")
