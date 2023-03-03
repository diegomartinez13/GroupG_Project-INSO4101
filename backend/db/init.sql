create table Users (
	user_id serial PRIMARY KEY,
	username VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(50) NOT NULL,
	reward_points INT NOT NULL DEFAULT 0,
	target_goal_amount DECIMAL(5,2) NOT NULL DEFAULT 0,
	target_goal_hours DECIMAL(5,2) NOT NULL DEFAULT 0,
	is_admin BOOLEAN NOT NULL DEFAULT false
);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('test', 'test', 475, 0.00, 0.00, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('njennens0', 'dPXU6vOMDZ1N', 475, 7.82, 20.94, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('nstodhart1', 'E7EZBC', 176, 95.12, 79.5, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('ltorvey2', '1MkYOPUuHUb', 924, 94.84, 64.9, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('eravenshaw3', 'N7P9EtnLp', 524, 96.06, 92.09, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('mkunath4', 'wgH9b71C', 787, 26.04, 94.83, false);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('dmckomb5', 'bOjUeR', 739, 7.93, 12.4, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('gburston6', 'JP4D1UA240pR', 852, 84.45, 48.44, false);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('wputten7', '4QcHm9Z33y', 361, 5.48, 52.78, true);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('bambroix8', 'Pea3mpGlAnRc', 119, 4.41, 85.57, false);
insert into Users (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values ('vcellone9', 'Du4xbz5f', 168, 26.56, 34.62, false);

create table RecyclingCenters (
	center_id serial PRIMARY KEY,
	information TEXT,
	location VARCHAR(50),
	coordinates POINT NOT NULL
);
insert into RecyclingCenters (information, location, coordinates) values ('Cras in purus eu magna vulputate luctus.', '2 Cardinal Circle', '(18.781063,-66.194474)');
insert into RecyclingCenters (information, location, coordinates) values ('Nullam sit amet turpis elementum ligula vehicula consequat.', '9 Steensland Parkway', '(18.419663,-66.547098)');
insert into RecyclingCenters (information, location, coordinates) values ('Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.', '6120 Granby Hill', '(18.153416,-66.810083)');
insert into RecyclingCenters (information, location, coordinates) values ('Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', '15692 Orin Road', '(18.620158,-66.336410)');
insert into RecyclingCenters (information, location, coordinates) values ('Morbi non quam nec dui luctus rutrum.', '1 Warbler Avenue', '(18.409101,-66.375284)');
insert into RecyclingCenters (information, location, coordinates) values ('Nam dui.', '8 Haas Street', '(18.464167,-66.602906)');
insert into RecyclingCenters (information, location, coordinates) values ('Nullam molestie nibh in lectus.', '1939 Butterfield Junction', '(18.918846,-66.231186)');
insert into RecyclingCenters (information, location, coordinates) values ('Phasellus sit amet erat.', '0 Mendota Junction', '(18.450534,-66.096305)');
insert into RecyclingCenters (information, location, coordinates) values ('Morbi non quam nec dui luctus rutrum.', '75646 New Castle Road', '(18.650560,-66.915351)');
insert into RecyclingCenters (information, location, coordinates) values ('Sed vel enim sit amet nunc viverra dapibus.', '7 6th Point', '(18.234532,-66.837181)');

create table Events (
	event_id serial PRIMARY KEY,
	name VARCHAR(75) NOT NULL,
	description TEXT,
	location VARCHAR(50),
	start_datetime TIMESTAMP NOT NULL,
	end_datetime TIMESTAMP NOT NULL
);
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (1, 'Community-wide recycling event for electronics', 'Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh. In hac habitasse platea dictumst.', '4 Red Cloud Lane', '2022-05-16 11:37:37', '2022-05-16 15:37:37');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (2, 'Recycling drop-off event for hazardous waste', 'Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh. Quisque id justo sit amet sapien dignissim vestibulum.', '93694 8th Center', '2022-12-19 22:34:10', '2022-12-20 01:34:10');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (3, 'Neighborhood paper recycling drive', 'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', '7378 Sundown Plaza', '2022-09-29 01:17:03', '2022-09-29 04:17:03');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (4, 'Plastic bottle collection event at a local park', 'Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit.', '76985 Helena Parkway', '2022-04-19 05:05:28', '2022-04-19 09:05:28');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (5, 'Composting workshop at a community garden', 'Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna.', '9431 Eastlawn Terrace', '2022-12-03 13:12:45', '2022-12-03 14:12:45');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (6, 'School-wide recycling competition', 'Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.', '262 Westerfield Circle', '2022-10-11 04:01:52',  '2022-10-11 05:01:52');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (7, 'Car battery and tire recycling event at a local garage', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', '0 Shelley Place', '2023-02-16 14:36:02', '2023-02-16 18:36:02');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (8, 'Recycling event for used cooking oil and grease', 'Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.', '67001 Grover Street', '2022-08-03 21:27:58', '2022-08-04 00:27:58');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (9, 'Clothing swap and donation event', 'Nam nulla.', '351 Golden Leaf Trail', '2023-05-09 17:44:03', '2023-05-09 18:44:03');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (10, 'Battery and small electronics recycling at a local library', 'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', '0 Toban Place', '2022-03-05 02:55:25', '2022-03-05 04:55:25');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (11, 'Community-wide cardboard and paperboard recycling drive', 'Fusce consequat. Nulla nisl. Nunc nisl.', '4656 Village Green Alley', '2023-03-30 16:19:50', '2023-03-30 18:19:50');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (12, 'Annual household hazardous waste disposal day', 'Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam. Nam tristique tortor eu pede.', '13287 Anniversary Court', '2022-09-16 07:43:04', '2022-09-16 11:43:04');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (13, 'Used book collection and exchange event at a community center', 'Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', '4 Havey Trail', '2023-04-13 07:41:33', '2023-04-13 11:41:33');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (14, 'Large appliance recycling event at a city dump', 'Phasellus in felis. Donec semper sapien a libero.', '9 Grayhawk Street', '2022-03-01 20:08:57', '2022-03-01 23:08:57');
insert into Events (event_id, name, description, location, start_datetime, end_datetime) values (15, 'Drop-off event for used ink cartridges and toners at an office supply store', 'Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.', '9 Melby Lane', '2023-02-13 03:36:09', '2023-02-13 06:36:09');

create table RecyclingEfforts (
	effort_id serial PRIMARY KEY,
	recycling_hours DECIMAL(3,2) NOT NULL DEFAULT 0,
	amount_recycled DECIMAL(5,2) NOT NULL DEFAULT 0,
	recycling_date DATE NOT NULL DEFAULT CURRENT_DATE,
	user_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (2.2, 53.02, '2022-10-30', 4);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (3.55, 60.08, '2022-04-13', 2);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (1.52, 40.6, '2022-08-17', 11);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (3.09, 89.4, '2022-04-22', 2);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (2.44, 16.23, '2022-04-25', 6);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (2.43, 24.38, '2022-04-09', 6);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (3.46, 88.64, '2023-01-18', 10);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (2.17, 11.9, '2022-08-30', 9);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values (3.13, 42.04, '2022-11-03', 7);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.01, 44.54, '2022-02-14', 9);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 1.27, 36.65, '2022-03-10', 7);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.78, 54.65, '2022-11-27', 9);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.16, 28.4, '2022-03-27', 4);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.11, 40.67, '2022-08-13', 2);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.4, 83.38, '2022-05-31', 7);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 1.24, 10.32, '2022-02-24', 8);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 1.21, 87.07, '2022-11-11', 8);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.81, 9.56, '2022-07-04', 4);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.61, 24.52, '2022-02-06', 3);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.25, 51.9, '2022-06-04', 4);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.43, 10.43, '2022-02-14', 3);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.61, 96.07, '2022-12-24', 4);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 1.87, 81.89, '2022-03-30', 7);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.07, 58.78, '2022-12-21', 8);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.66, 94.37, '2022-08-10', 3);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.79, 9.74, '2022-06-23', 3);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 1.08, 19.18, '2023-01-18', 3);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.98, 75.19, '2022-03-02', 8);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 3.52, 66.2, '2022-02-18', 9);
insert into RecyclingEfforts (recycling_hours, amount_recycled, recycling_date, user_id) values ( 2.08, 25.64, '2022-12-23', 3);

create table Posts (
	post_id serial PRIMARY KEY,
	title TEXT NOT NULL,
	content TEXT NOT NULL,
	created_at DATE NOT NULL DEFAULT CURRENT_DATE,
	parent_post_id INT,
	user_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (1, 'Vivamus tortor.', 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.

Fusce consequat. Nulla nisl. Nunc nisl.

Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.', '2023-01-28 13:26:43', 12, 7);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (2, 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante.', 'Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.', '2022-02-01 18:01:38', 7, 9);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (3, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam.', 'Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.

Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.', '2022-09-01 16:41:49', 1, 11);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (4, 'Praesent id massa id nisl venenatis lacinia.', 'Phasellus in felis. Donec semper sapien a libero. Nam dui.

Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.', '2022-01-19 19:50:19', 17, 6);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (5, 'Maecenas rhoncus aliquam lacus.', 'In congue. Etiam justo. Etiam pretium iaculis justo.

In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.

Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.', '2023-02-28 20:17:28', 3, 8);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (6, 'Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.', 'Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.

Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.', '2023-03-02 16:24:36', 2, 8);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (7, 'Morbi non quam nec dui luctus rutrum.', 'In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.', '2022-04-07 02:42:38', 15, 1);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (8, 'Aliquam erat volutpat.', 'Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.

Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.

Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.', '2022-04-09 00:25:09', 20, 1);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (9, 'Integer ac leo.', 'Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.', '2022-11-19 04:54:21', 12, 8);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (10, 'In hac habitasse platea dictumst.', 'In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.

Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', '2022-10-16 23:48:59', 10, 5);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (11, 'Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.', 'Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.', '2022-03-12 13:13:03', 20, 7);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (12, 'Donec ut mauris eget massa tempor convallis.', 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.

Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', '2022-07-22 15:33:49', 16, 10);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (13, 'Vivamus vestibulum sagittis sapien.', 'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.

Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', '2022-07-03 21:07:28', 2, 2);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (14, 'Aenean fermentum.', 'Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.', '2023-01-22 13:07:51', 7, 9);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (15, 'Morbi non quam nec dui luctus rutrum.', 'Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.

In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.

Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', '2023-01-16 22:04:40', 10, 11);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (16, 'Nulla justo.', 'Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.

In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.

Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', '2022-08-12 00:24:08', 4, 10);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (17, 'Integer a nibh.', 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', '2022-11-18 02:46:43', 17, 6);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (18, 'Nulla ut erat id mauris vulputate elementum.', 'Phasellus in felis. Donec semper sapien a libero. Nam dui.

Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.', '2022-03-04 01:00:52', 8, 3);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (19, 'In hac habitasse platea dictumst.', 'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.

Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.

Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.', '2022-10-10 23:20:51', 4, 4);
insert into Posts (post_id, title, content, created_at, parent_post_id, user_id) values (20, 'In congue.', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.

Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.', '2023-02-11 10:59:51', 9, 3);

create table HasReaction (
	user_id INT NOT NULL,
	post_id INT NOT NULL,
	is_liked BOOLEAN,
	UNIQUE (user_id, post_id),
	FOREIGN KEY (user_id) REFERENCES Users(user_id),
	FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);
insert into HasReaction (user_id, post_id, is_liked) values (11, 16, true);
insert into HasReaction (user_id, post_id, is_liked) values (1, 8, true);
insert into HasReaction (user_id, post_id, is_liked) values (3, 8, false);
insert into HasReaction (user_id, post_id, is_liked) values (3, 3, true);
insert into HasReaction (user_id, post_id, is_liked) values (11, 17, true);
insert into HasReaction (user_id, post_id, is_liked) values (3, 1, true);
insert into HasReaction (user_id, post_id, is_liked) values (8, 11, true);
insert into HasReaction (user_id, post_id, is_liked) values (4, 9, false);
insert into HasReaction (user_id, post_id, is_liked) values (7, 18, false);
insert into HasReaction (user_id, post_id, is_liked) values (4, 11, true);
insert into HasReaction (user_id, post_id, is_liked) values (10, 4, false);
insert into HasReaction (user_id, post_id, is_liked) values (7, 19, false);
insert into HasReaction (user_id, post_id, is_liked) values (5, 2, true);
insert into HasReaction (user_id, post_id, is_liked) values (3, 9, true);
insert into HasReaction (user_id, post_id, is_liked) values (9, 8, true);
insert into HasReaction (user_id, post_id, is_liked) values (5, 14, false);
insert into HasReaction (user_id, post_id, is_liked) values (5, 11, false);
insert into HasReaction (user_id, post_id, is_liked) values (11, 4, true);
insert into HasReaction (user_id, post_id, is_liked) values (10, 18, false);
insert into HasReaction (user_id, post_id, is_liked) values (7, 16, true);
insert into HasReaction (user_id, post_id, is_liked) values (10, 1, false);
insert into HasReaction (user_id, post_id, is_liked) values (8, 3, false);
insert into HasReaction (user_id, post_id, is_liked) values (3, 5, false);
insert into HasReaction (user_id, post_id, is_liked) values (4, 7, false);
insert into HasReaction (user_id, post_id, is_liked) values (9, 2, true);
insert into HasReaction (user_id, post_id, is_liked) values (2, 12, true);
insert into HasReaction (user_id, post_id, is_liked) values (9, 1, true);
insert into HasReaction (user_id, post_id, is_liked) values (11, 12, false);
insert into HasReaction (user_id, post_id, is_liked) values (4, 16, true);
insert into HasReaction (user_id, post_id, is_liked) values (11, 8, true);
insert into HasReaction (user_id, post_id, is_liked) values (3, 13, true);
insert into HasReaction (user_id, post_id, is_liked) values (1, 6, true);
insert into HasReaction (user_id, post_id, is_liked) values (2, 20, false);
insert into HasReaction (user_id, post_id, is_liked) values (6, 10, false);
insert into HasReaction (user_id, post_id, is_liked) values (4, 10, true);
insert into HasReaction (user_id, post_id, is_liked) values (5, 6, true);
insert into HasReaction (user_id, post_id, is_liked) values (2, 11, true);
insert into HasReaction (user_id, post_id, is_liked) values (1, 20, true);
insert into HasReaction (user_id, post_id, is_liked) values (2, 2, false);
insert into HasReaction (user_id, post_id, is_liked) values (8, 1, true);
insert into HasReaction (user_id, post_id, is_liked) values (3, 2, false);
insert into HasReaction (user_id, post_id, is_liked) values (4, 2, false);
insert into HasReaction (user_id, post_id, is_liked) values (8, 12, true);
insert into HasReaction (user_id, post_id, is_liked) values (4, 19, true);
insert into HasReaction (user_id, post_id, is_liked) values (5, 3, true);
insert into HasReaction (user_id, post_id, is_liked) values (1, 10, true);
insert into HasReaction (user_id, post_id, is_liked) values (4, 15, true);
