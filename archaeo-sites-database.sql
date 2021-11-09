BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Nom"	TEXT NOT NULL,
	"Login"	TEXT NOT NULL UNIQUE,
	"Email"	TEXT NOT NULL UNIQUE,
	"Mdp"	TEXT NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sites" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Nom"	TEXT NOT NULL,
	"Adresse"	TEXT NOT NULL,
	"Latitude"	INTEGER NOT NULL,
	"Longitude"	INTEGER NOT NULL,
	"Description"	TEXT,
	"Periode"	INTEGER,
	"Lien"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "images" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Source"	TEXT,
	"Image"	TEXT,
	"IdSite"	INTEGER,
	"Legende"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT),
	FOREIGN KEY("IdSite") REFERENCES "sites"("Id")
);
INSERT INTO "user" ("Id","Nom","Login","Email","Mdp") VALUES (1,'Bristow','rebeccabristow','rebecca.bristow@chartes.psl.eu','pbkdf2:sha256:150000$0tBldI83$e43535b01c0dc66b53ddedcd2a4325252a9d8d810ba85150fba3556e8a87ac9f'),
 (2,'Rebecca','rebecca','beccabristow@hotmail.fr','pbkdf2:sha256:260000$MPVREYvCdhkqmRvS$6d216e307bd621da09976e5ac26fc91c0bca8dbfca906a047be1e6b73789f624');
INSERT INTO "sites" ("Id","Nom","Adresse","Latitude","Longitude","Description","Periode","Lien") VALUES (1,'Les catacombes','1 Avenue du Colonel Henri Rol-Tanguy, 75014 Paris',48.833927154541,2.33218312263489,'Sous les rues de Paris se trouvent d''anciennes galeries de carrières, véritable labyrinthe souterrain. Il s''agit également du plus grand ossuaire du monde, ouvert au public depuis 1809.','XVIIIe au XIXe siècle','http://catacombes.paris.fr/
'),
 (2,'La crypte archéologique de l’île de la Cité','7 Parvis Notre-Dame - Pl. Jean-Paul II, 75004 Paris',48.8539489,2.3477596,'La crypte archéologique de la Cité se trouve sous le parvis de la cathédrale Notre-Dame de Paris. Les fouilles réalisées dans les années soixante y ont mis au jour des bâtiments datant de l''Antiquité jusqu''au XXe siècle, retraçant l''histoire de l''île de la Cité. On peut notamment y découvrir les vestiges du port de l''antique Lutèce, les restes médiévaux de la rue Neuve Notre-Dame ou encore le tracé des égouts haussmaniens. ','Ier siècle au XIXe siècle','http://www.crypte.paris.fr/la-crypte/la-crypte/plus-de-2000-ans-d-histoire
'),
 (3,'Sanctuaire Gallo-Romain des Vaux de la Celle','10 Rue de Champagne, 95420 Genainville',49.1227951049805,1.75456619262695,'Le sanctuaire des Vaux de la Celle à Genainville est un site gallo-romain composé d''un temple, de bassins monumentaux et d’un théâtre. Ses objets sont exposés au musée archéologique du Val d’Oise à Guiry-en-Vexin.','Antiquité','http://www.pnr-vexin-francais.fr/fr/education-et-culture/valorisation-patrimoines/genainville/'),
 (4,'Site d’Orville','Chemin d''Orville, 95380 Louvres',49.0313,2.558,'Le chateau médiéval d''Orville a connu plusieurs phases de fortification, aux 13e et 14e siècles, avant d''être assiégé et détruit durant la guerre de Cent ans. Des fouilles archéologiques y ont aussi mis au jour des vestiges datant du 8e et 9e siècles. ','VIIe au Xe siècle','https://archea.roissypaysdefrance.fr/quest-quarchea/le-site-dorville'),
 (5,'Site Archéologique de Gisacum - Le Vieil-Evreux','8 Rue des Thermes, 27930 Le Vieil-Évreux',49.0046946,1.2329226,'Le site archéologique de Gisacum représente une importante ville sanctuaire gallo-romaine. Capitale religieuse des Aulerques Eburovices, Gisacum disposait de nombreux édifices publics (sanctuaire, thermes, théâtre, etc.). Elle fut fondée au début du 1er siècle après J.-C. et abandonnée dès la deuxième moitié du 3ème siècle. ','Antiquité','http://www.gisacum-normandie.fr/'),
 (6,'Dolmen de la pierre Ardoue','78610 Saint-Léger-en-Yvelines',48.7226014,1.7637028,'La Pierre Ardoue, aussi appelée Pierre Ardroue ou Pierre Ardoué, est un dolmen situé à Saint-Léger-en-Yvelines. Le dolmen se trouve au cœur forêt de Rambouillet, à 1,5 km au nord-ouest du village de Saint-Léger-en-Yvelines et à l''ouest des Buttes Rouges. Il est constitué d''une table en grès, dont le gisement le plus proche est situé à 2 km du site.

L''état de dégradation de l''édifice ne permet pas de comprendre clairement son architecture. Deux des quatre orthostates sont encore en place tandis les deux autres se sont affaissés sous la table. Celle-ci repose directement sur le sol. Les dimensions de la chambre et l''orientation de son ouverture demeurent inconnues. Il ne s''agit probablement pas d''une allée couverte mais d''un dolmen rectangulaire dit de type beauceron. Aucune trace de tumulus n''est visible, les débris visibles aux alentours étant ceux d''une ancienne bâtisse rurale désormais détruite.
La couche archéologique ayant été retirée bien antérieurement, aucun mobilier ou ossement n''a été retrouvé.
','Néolithique',''),
 (7,'Dolmen des Trois Pierres','60590 Trie-Château',49.285212,1.8131792,'Le dolmen des Trois Pierres est situé dans le centre ville de Saint-Nazaire (Loire-Atlantique). Il se trouve sur la place du Dolmen, à l''intersection de la rue du Dolmen et de la rue du Menhir. Il est constitué de deux pierres verticales sur lesquelles repose une troisième pierre horizontale et s''élève à environ 3 m de haut. Plusieurs autres pierres sont également situées à proximité immédiate. ','Néolithique',''),
 (8,'Dolmen de la pierre levée','91510, Janville-sur-Juine',48.5145802,2.2620863,'Le dolmen de la Pierre Levée, aussi appelé dolmen de Janville ou dolmen de Pocancy, est situé à Janville-sur-Juine (Essonne). Il s''agit d''un dolmen simple orienté est-ouest et ouvrant à l''est. Les deux dalles en façade correspondaient peut-être à un portique. Des rainures sont visibles sur l''arrière de la table de couverture ; il s''agissait peut-être des sillons d''un polissoir, ou plus vraisemblablement à des gravures abstraites.','Néolithique',''),
 (9,'Dolmen de Rumont (Seine-et-Marne).','77760 Rumont',48.2666741,2.4991629,'Dolmen dit la Pierre l''Armoire.','Néolithique',NULL),
 (10,'Musée d’Archéologie Nationale','Domaine National de Saint-Germain-en-Laye, Château - Place Charles de Gaulle, 78100 Saint-Germain-en-Laye',48.897834777832,2.09550261497498,'Le musée national d''archéologie est créé en 1867 sous le nom de musée des antiquités nationales. Installé au château de Saint-Germain-en-Laye (Yvelines), il présente des collections datées du Paléolithique jusqu''à l''Antiquité. Le musée possède par ailleurs une salle dite d''archéologie comparée, créée au XXe siècle et réunissant plusieurs collections ethnographiques.','Paléolithique - XXe siècle','https://musee-archeologienationale.fr/'),
 (11,'Musée archéologique du Val d''Oise','4 Place du Château, 95450 Guiry-en-Vexin',49.1087468,1.8497408,'Le musée archéologique du Val-d''Oise est situé à Guiry-en-Vexin, à 50 km environ du nord-ouest de Paris. Il réunit les découvertes archéologiques du Val d''Oise, datées du paléolithique jusqu''au XXe siècle. On peut notamment y observer la plus importante collection de stèles mérovingiennes de France. 

Ses réserves accueillent à ce jour plus de 20 000 objets archéologiques en cours d''étude ou de valorisation. ','Paléolithique - XXe siècle','https://www.valdoise.fr/608-le-musee-archeologique-departemental-du-val-d-oise.htm');
INSERT INTO "images" ("Id","Source","Image","IdSite","Legende") VALUES (1,'https://fr.wikipedia.org/wiki/Catacombes_de_Paris#/media/Fichier:Paris_Catacombs_Entrance.jpg','img/imgSites/catacombes1.jpg',1,'Entrée des catacombes de Paris, pavillon n° 3 de la barrière d''Enfer, place Denfert-Rochereau.'),
 (2,'https://fr.wikipedia.org/wiki/Catacombes_de_Paris#/media/Fichier:Catacombes_de_Paris_-_Passage_dit_des_doubles_carri%C3%A8res_1.jpg','img/imgSites/catacombes2.jpg',1,'Le passage dit des doubles carrières précède l''ossuaire.'),
 (3,'https://fr.wikipedia.org/wiki/Crypte_arch%C3%A9ologique_de_l%27%C3%AEle_de_la_Cit%C3%A9#/media/Fichier:La_crypte_arch%C3%A9ologique_du_Parvis_de_Notre-Dame_(Paris)_(8274683584).jpg','img/imgSites/crypte1.jpg',2,'Thermes de la crypte.'),
 (4,'http://www.pnr-vexin-francais.fr/fr/education-et-culture/valorisation-patrimoines/genainville/','img/imgSites/vaux1.jpg',3,'Vue du temple.'),
 (5,'https://archea.roissypaysdefrance.fr/quest-quarchea/le-site-dorville','img/imgSites/orville1.jpg',4,NULL),
 (6,'http://www.gisacum-normandie.fr/','img/imgSites/gisacum1.jpg',5,NULL),
 (7,'https://fr.wikipedia.org/wiki/Pierre_Ardoue#/media/Fichier:Dolmen_de_la_Pierre_Ardoue_1.JPG','img/imgSites/ardoue1.jpg',6,NULL),
 (8,'https://fr.wikipedia.org/wiki/Pierre_Lev%C3%A9e_(Janville-sur-Juine)#/media/Fichier:Dolmen_dit_de_la_Pierre-Lev%C3%A9e.jpg','img/imgSites/janville1.jpg',8,NULL),
 (9,'https://fr.wikipedia.org/wiki/Fichier:Dolmen_de_Rumont.jpg','img/imgSites/rumont1.jpg',9,NULL),
 (10,'https://fr.wikipedia.org/wiki/Dolmen_des_Trois_Pierres_(Saint-Nazaire)#/media/Fichier:Dolmen_des_Trois_Pierres,_Saint-Nazaire_-_Rear_View_01.JPG','img/imgSites/troispierres1.jpg',7,NULL),
 (11,'https://musee-archeologienationale.fr/','img/imgSites/man1.jpg',10,NULL),
 (12,'https://fr.wikipedia.org/wiki/Mus%C3%A9e_arch%C3%A9ologique_du_Val-d%27Oise#/media/Fichier:Mus%C3%A9e_arch%C3%A9ologique_d%C3%A9partemental_du_Val-d''Oise.jpg','img/imgSites/valdoise1.jpg',11,NULL),
 (13,'https://www.inrap.fr/decouvrir-le-musee-archeologique-du-val-d-oise-11561','img/imgSites/valdoise2.jpg',11,NULL);
COMMIT;
