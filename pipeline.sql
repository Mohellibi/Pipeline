create database Ecole;
Use Ecole;


create table élèves (
    student_id int primary key,
    prenom varchar(50),
    nom varchar(50),
    numero_salle varchar(10),
    telephone varchar(15) not null unique,
    email varchar(100) unique,
    annee_obtention int,
    numero_classe varchar(10)
);

create table enseignants (
    teacher_id int primary key,
    prenom varchar(50),
    nom varchar(50),
    numero_salle varchar(10),
    departement varchar(50),
    annee_obtention int,
    email varchar(100) unique,
    telephone varchar(15) not null unique,
    numero_classe varchar(10)
);


insert into enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
values (1, 'jonas', 'salk', null, 'biologie', null, 'jsalk@school.org', '777-555-4321', '5');
insert into élèves (student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
values (1, 'mark', 'watney', null, '777-555-1234', null, 2035, '5');

insert into enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
values 
(2, 'sophie', 'dubois', null, 'mathématiques', null, 'sophie.dubois@school.org', '777-555-1111', '1'),
(3, 'paul', 'martin', null, 'physique', null, 'paul.martin@school.org', '777-555-2222', '2'),
(4, 'lucie', 'bernard', null, 'chimie', null, 'lucie.bernard@school.org', '777-555-3333', '3'),
(5, 'antoine', 'roux', null, 'histoire', null, 'antoine.roux@school.org', '777-555-4444', '4');

insert into élèves (student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
values 
(2, 'alice', 'durand', '101', '777-555-1112', 'alice.durand@school.org', 2035, '1'),
(3, 'benjamin', 'moreau', '101', '777-555-1113', 'benjamin.moreau@school.org', 2035, '1'),
(4, 'camille', 'giraud', '101', '777-555-1114', 'camille.giraud@school.org', 2035, '1'),
(5, 'david', 'leclerc', '101', '777-555-1115', 'david.leclerc@school.org', 2035, '1'),
(6, 'emma', 'lafont', '101', '777-555-1116', 'emma.lafont@school.org', 2035, '1'),
(7, 'florian', 'muller', '101', '777-555-1117', 'florian.muller@school.org', 2035, '1'),
(8, 'garance', 'perez', '101', '777-555-1118', 'garance.perez@school.org', 2035, '1'),

(9, 'hugo', 'fontaine', '201', '777-555-2111', 'hugo.fontaine@school.org', 2035, '2'),
(10, 'ines', 'chevalier', '201', '777-555-2112', 'ines.chevalier@school.org', 2035, '2'),
(11, 'jules', 'noel', '201', '777-555-2113', 'jules.noel@school.org', 2035, '2'),
(12, 'laura', 'morris', '201', '777-555-2114', 'laura.morris@school.org', 2035, '2'),
(13, 'mathis', 'robin', '201', '777-555-2115', 'mathis.robin@school.org', 2035, '2'),

(14, 'karl', 'boucher', '301', '777-555-3111', 'karl.boucher@school.org', 2035, '3'),
(15, 'lola', 'ricard', '301', '777-555-3112', 'lola.ricard@school.org', 2035, '3'),
(16, 'maxime', 'vasseur', '301', '777-555-3113', 'maxime.vasseur@school.org', 2035, '3'),

(17, 'nina', 'francois', '401', '777-555-4111', 'nina.francois@school.org', 2035, '4'),
(18, 'olivier', 'garnier', '401', '777-555-4112', 'olivier.garnier@school.org', 2035, '4'),
(19, 'pauline', 'delacroix', '401', '777-555-4113', 'pauline.delacroix@school.org', 2035, '4'),
(20, 'quentin', 'marcel', '401', '777-555-4114', 'quentin.marcel@school.org', 2035, '4'),
(21, 'rose', 'simon', '401', '777-555-4115', 'rose.simon@school.org', 2035, '4'),
(22, 'simon', 'leroy', '401', '777-555-4116', 'simon.leroy@school.org', 2035, '4'),
(23, 'tania', 'guillot', '401', '777-555-4117', 'tania.guillot@school.org', 2035, '4'),
(24, 'victor', 'blais', '401', '777-555-4118', 'victor.blais@school.org', 2035, '4'),
(25, 'wendy', 'valentin', '401', '777-555-4119', 'wendy.valentin@school.org', 2035, '4'),
(26, 'xavier', 'richard', '401', '777-555-4120', 'xavier.richard@school.org', 2035, '4'),

(27, 'yasmine', 'clement', '501', '777-555-5111', 'yasmine.clement@school.org', 2035, '5'),
(28, 'zacharie', 'fortier', '501', '777-555-5112', 'zacharie.fortier@school.org', 2035, '5'),
(29, 'amandine', 'barre', '501', '777-555-5113', 'amandine.barre@school.org', 2035, '5'),
(30, 'benoit', 'blanchard', '501', '777-555-5114', 'benoit.blanchard@school.org', 2035, '5'),
(32, 'dorian', 'couture', '501', '777-555-5116', 'dorian.couture@school.org', 2035, '5'),
(33, 'emilie', 'gagne', '501', '777-555-5117', 'emilie.gagne@school.org', 2035, '5'),
(34, 'fabien', 'caron', '501', '777-555-5118', 'fabien.caron@school.org', 2035, '5');
