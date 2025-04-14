from pyad import adquery, pyadutils

def get_expiry_days(username):
    try:
        date_expiry = None
        date = None
        q = adquery.ADQuery()
        q.execute_query(attributes=['userPrincipalName', 'msDS-UserPasswordExpiryTimeComputed'],
                        where_clause=f"objectClass = 'user' and sAMAccountName = '{username}'",
                        base_dn="DC=sogaz,DC=ru", type='LDAP', page_size=100)

        for row in q.get_results():
            date_expiry = row['msDS-UserPasswordExpiryTimeComputed']

        if date_expiry:
            date = pyadutils.convert_datetime(date_expiry).strftime("%d-%m-%Y")

        return date

    except Exception as err:
        return 0

    