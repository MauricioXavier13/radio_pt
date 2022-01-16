# radio_pt
Play your portuguese radio stations in your media players (google compatible)

-----------------------------------------------------------------------------------

### Credits to
https://github.com/maxcalavera81/radios for the original idea!

A big thank you to Pedro Miguel Fernandes (https://github.com/pmfernandes) for the contribution with the python scripts.

--------------------------------------------------------------------------------------

#Pre-requisites:

HACS Custom-Cards:

custom:button-card | https://github.com/custom-cards/button-card
custom:swipe-card | https://github.com/bramkragten/swipe-card
card-tools | https://github.com/thomasloven/lovelace-card-tools
mini-media-player | https://github.com/kalkih/mini-media-player

# Step by Step installation

1. Copy all the python scripts (.py) to your folder (config/python_scripts) in HA;
	- Don't forget to enable it in in your configuration.yaml file writing:
	```
	python_script:
	```
2. Confirm that you have the repository config/www/downloads/ or set another one in variable filename in all the python radio files,
3. Download the logos folder. *I'm using /local(www)/radio_logo/ path in my lovelace card.*
4. Download the icons (media player) folder. *I'm using /local(www)/icon/ path in my lovelace card.*
5. Download de folder Radio with all the Scripts and Sensors. You can use it as a [package configuration](https://www.home-assistant.io/docs/configuration/packages/);
	- *In this version, an independent folder was created for each media player. So you can copy a single folder or 2 or how many you just want.*
	- In each media folder:
		- In radio_stations-XXXX.yaml, sensors_radio_XXXX_playing.yaml, scripts_radio_set_info_media_player_XXXX.yaml and automation_radio_XXXX.yaml, change all the entity_id fields to your media players.
6. Create one entity helper named *input_number.speaker_radio*. Minimum 1 and Max 100 will be enough! :) 
7. Copy the lovelace_card code and enter in a manual card. Change your media_player entities and the respective service in each radio button (see lovelace_card for more detailed instructions);
8. The automation will trigger everytime you handle with the media player. The media player is trying to override your data with the default one, and with this automation you also will override with the radio info.
9. Enjoy! :)

## DISCLAIMER
Some radios don't have all the info available;
You can have many errors and warning related to those sensors, even if they are not playing any music and the scrape sensor is not catching any data to show;

# Main Card - Global View

![image](https://user-images.githubusercontent.com/74264882/149369755-db5562fe-23e3-4867-b826-f5364127118e.png)

------------------------------------------------------------------------------------------------------------------------

![image](https://user-images.githubusercontent.com/74264882/149369857-689b60e9-c31b-4094-9283-8169f6227dd0.png)


# Live now (All Stations Info)

![image](https://user-images.githubusercontent.com/74264882/149369994-25b189e2-97ce-432a-842a-f3c0b360f330.png))
