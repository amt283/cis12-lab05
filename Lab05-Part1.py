def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and i_part != 0:
            return False
        return 0 <= i_part <= 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True

# print(is_valid_part('127'), is_valid_part('AAA'), is_valid_part('-127'), is_valid_part('01'), is_valid_part('02'), is_valid_part('0'))

print(is_valid_ip('198.162.0.1'),
      is_valid_ip('198.162.0.1.2'),
      is_valid_ip('280.162.0.1.2'),
      is_valid_ip('198.162.0'),
      )
