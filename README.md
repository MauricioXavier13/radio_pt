# radio_pt
Play your portuguese radio stations in your media players (google compatible)

Credits to https://github.com/maxcalavera81/radios for the original idea!
A big thank you to Pedro Miguel Fernandes (https://github.com/pmfernandes) for the contribution with the python scripts.

Step by Step installation

1. Copy all the python scripts (.py) to your folder in HA;
	a. Don't forget to enable it in in your configuration.yaml file writing (python_script:);
2. Confirm that you have the repository config/www/downloads/ or set another one in variabel filename in all the python radio files,
3. Download the logos folder. I'm using /local(www)/radio_logo/ path in my lovelace card. 
4. Download de folder Radio with Scripts and Sensors. You can use it as a package configuration;
	a. In radio_stations.yaml and radio_set_info_media_player.yaml change all the entity_id fields to your media players.
5. Copy the automation and change the entity_id to your media player. This will trigger everytime you handle with the media player he is trying to override your data with the default one, and with this automation you also will override with the radio info.
6. Copy the lovelace_card code and enter in a manual card. Change your media_player entity...
7. Enjoy! :)

# Main Card - Global View

![image](https://user-images.githubusercontent.com/74264882/113280023-b3fb0e00-92db-11eb-95f8-15b78891ace8.png)

![image](https://user-images.githubusercontent.com/74264882/113280115-d12fdc80-92db-11eb-9597-d6629372e797.png)


# Live now (All Stations Info)

![image](https://user-images.githubusercontent.com/74264882/112849065-9c841100-90a0-11eb-90f8-0972fd687fb9.png)


