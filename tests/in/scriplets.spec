%post -n %libname -p /sbin/ldconfig

%post
/sbin/ldconfig

%post -n %{_libname}
/sbin/ldconfig

%post
/sbin/ldconfig
someothercommand
