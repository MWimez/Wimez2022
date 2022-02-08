########### Mathilde Wimez ##########

## This is a worflow of the recursive template matching method ##
## This is not a unique way to make this matched-filter search ##
## For more details refer to the Wimez & Frank, JGR, 2022 ##

# loading the first template for matched-filter search
[template_waveforms, moveout] = load_first_template()

# run the firt matched-filter search
# fmf refers to Eric Beaucé and William Frank Fast matched-filter search
for d in range(n_days_data):
    # loading the data by day 
	day_data = load_day_data(d)
    # matched-filter search of event
	cc_sum = fast_matched_filter(template_waveforms, moveout, day_data)
	
    # detections output to vary depending on the interest in the study
	[detection_times, cc, ampl] = extract_detections(cc_sum)

# extraction of the new templates with specific requirements
[new_templates, moveout] = extract_new_templates(detection_times, cc, ampl)
n = new_templates.len()

# run the matched-filter search until no more templates exist
while n > 0
	for d in range(n_days_data):
		day_data = load_day_data(d)
		cc_sum = fast_matched_filter(template_waveforms, moveout, day_data))
	
		[detection_times, cc, ampl] = extract_detections(cc_sum)

	[new_templates, moveout] = extract_new_templates(detection_times, cc, ampl)
    n = new_templates.len()