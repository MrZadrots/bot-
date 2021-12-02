create table if not exists applications
(
    chat_id   bigint            not null,
    username  text,
    application_image text,
    application_description text,
    application_status integer default 0 not null,
    id        serial            not null             primary key
);

alter table applications
    owner to postgres;

create unique index if not exists applications_id_uindex
    on applications (id);
