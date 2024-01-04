
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'News');
INSERT INTO `category` VALUES ('2', 'Education');
INSERT INTO `category` VALUES ('3', 'Society');
INSERT INTO `category` VALUES ('4', 'Entertainment');
INSERT INTO `category` VALUES ('5', 'Others');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '123456', 'Admin');

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `path` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `picture` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of video
-- ----------------------------
INSERT INTO `video` VALUES ('1', '1', 'CKplayer', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('2', '1', 'Cat', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat1.jpg');
INSERT INTO `video` VALUES ('3', '1', 'Cat 2', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('4', '2', 'Wolf', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('5', '1', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('6', '2', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('7', '3', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat1.jpg');
INSERT INTO `video` VALUES ('8', '4', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('9', '5', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('10', '5', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('11', '3', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('12', '1', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('13', '2', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('14', '1', 'CKplayer', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('15', '1', 'Cat', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat1.jpg');
INSERT INTO `video` VALUES ('16', '1', 'Cat 2', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('17', '2', 'Wolf', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('18', '1', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('19', '2', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('20', '3', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat1.jpg');
INSERT INTO `video` VALUES ('21', '4', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('22', '5', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('23', '5', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
INSERT INTO `video` VALUES ('24', '3', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\wolf.jpg');
INSERT INTO `video` VALUES ('25', '1', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\cat2.jpg');
INSERT INTO `video` VALUES ('26', '2', 'Movie', 'http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', '\\upload\\img\\20180101\\eb048d7839442d0.png');
