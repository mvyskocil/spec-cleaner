#
# spec file for package multilinedefine
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define postInstall() \
. %{_sysconfdir}/selinux/config; \
if [ -e %{_sysconfdir}/selinux/%{2}/.rebuild ]; then \
   rm %{_sysconfdir}/selinux/%{2}/.rebuild; \
   (cd %{_sysconfdir}/selinux/%{2}/modules/active/modules; rm -f shutdown.pp amavis.pp clamav.pp gnomeclock.pp matahari.pp xfs.pp kudzu.pp kerneloops.pp execmem.pp openoffice.pp ada.pp tzdata.pp hal.pp hotplug.pp howl.pp java.pp mono.pp moilscanner.pp gamin.pp audio_entropy.pp audioentropy.pp iscsid.pp polkit_auth.pp polkit.pp rtkit_daemon.pp ModemManager.pp telepathysofiasip.pp ethereal.pp passanger.pp qpidd.pp pyzor.pp razor.pp pki-selinux.pp phpfpm.pp consoletype.pp ctdbd.pp fcoemon.pp isnsd.pp l2tp.pp rgmanager.pp corosync.pp aisexec.pp pacemaker.pp ) \
   %{_sbindir}/semodule -B -n -s %{2}; \
else \
    touch %{_sysconfdir}/selinux/%{2}/modules/active/modules/sandbox.disabled \
fi; \
if [ "${SELINUXTYPE}" == "%{2}" ]; then \
   if selinuxenabled; then \
      load_policy; \
   else \
      # selinux isn't enabled \
      # (probably a first install of the policy) \
      # -> we can't load the policy \
      true; \
   fi; \
fi; \
if selinuxenabled; then \
   if [ %{1} -eq 1 ]; then \
      /sbin/restorecon -R /root %{_localstatedir}/log %{_localstatedir}/run 2> /dev/null; \
   else \
      %{relabel} %{2} \
   fi; \
else \
   # run fixfiles on next boot \
   touch /.autorelabel \
fi;
Name:           multilinedefine


