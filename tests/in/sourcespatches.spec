

Source15: anothersource.tar.xz
source: testfile.tar.bz2
# This patch is improperly described but we are okay with it
Patch10: test2
%bcond_with self_hosting
Source2: testfile2.tar.bz2
Patch: test
# this is crazy define
%define root %version
%global test somethingelse

%prep
%setup -qn %name-%version
%setup -q -n "%name-%version" -a1
%setup -n "%name-%version" -q -b2
%setup -q -n %{name}-%{version}-src
%patch10 -p4
%patch -p1
