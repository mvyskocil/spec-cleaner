BuildRequires: iii  <=     4.2.1 jjj>  %{version} eee=%{version}-%{release} bbb
BuildRequires:      aaa<3.2.1 zzz
BuildRequires:    rrr >= %{version} kkk

Requires: iii  <=     4.2.1 jjj>  %{version} eee=%{version}-%{release} bbb
Requires:      aaa<3.2.1 zzz     pkgconfig(glib-2.0) perl(DBD::SQLite)
Requires:    rrr >= %{version} kkk

PreReq: iii  <=     4.2.1 jjj>  %{version} eee=%{version}-%{release} bbb
PreReq:      aaa<3.2.1 zzz
PreReq:    rrr >= %{version} kkk
