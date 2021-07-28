from astroquery.gaia import Gaia

table_list = Gaia.load_tables(only_names=True)

for table in table_list:
    print(table.get_qualified_name())
