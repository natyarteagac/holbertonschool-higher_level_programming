-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
CREATE DATABASE hbtn_0d_tvshows
USE hbtn_0d_tvshows
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"
SELECT * FROM tv_shows.title, tv_show_genres.id;
