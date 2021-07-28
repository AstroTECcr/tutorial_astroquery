from astroquery.gaia import Gaia

job = Gaia.launch_job("select top 100 "
                       "solution_id,ref_epoch,ra_dec_corr,astrometric_n_obs_al, "
                       "matched_observations,duplicated_source,phot_variable_flag "
                       "from gaiadr2.gaia_source order by source_id",
                       dump_to_file=True, output_format='csv')

r = job.get_results()
print(r['solution_id'])
