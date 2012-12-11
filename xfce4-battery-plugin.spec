%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Battery monitor plugin for the Xfce panel
Name:		xfce4-battery-plugin
Version:	1.0.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-battery-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	perl(XML::Parser)

%description
Battery monitor panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache
chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3mdv2012.0
+ Revision: 791521
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 790032
- Rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 633061
- update to new version 1.0.0
- drop patches 2 and 3
- drop old scriplets
- fix file list
- update url for Source0

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-7mdv2011.0
+ Revision: 615565
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-6mdv2010.1
+ Revision: 543416
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-5mdv2010.0
+ Revision: 445973
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - scriplets are now handles by filetriggers

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-3mdv2009.1
+ Revision: 349444
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-2mdv2009.1
+ Revision: 294988
- rebuild for new Xfce4.6 beta1

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2009.0
+ Revision: 280983
- update to new version 0.5.1
- drop patches 0 and 1 as they were fixed upstream

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-9mdv2009.0
+ Revision: 269783
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-8mdv2009.0
+ Revision: 194473
- merge patch 3 and 4 into one patch
- Patch3: rediff
- Patch4: fix apm_bios.h header placement

* Sun Feb 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-7mdv2008.1
+ Revision: 161855
- Patch0: fixes against kernel-2.6.21 and above
  Patch3: fixes against kernel-2.6.24

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Jérôme Soyer <saispo@mandriva.org> 0.5.0-6mdv2008.1
+ Revision: 116032
- Add two patches for lower acpi and us sysfs if available

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-5mdv2008.1
+ Revision: 110098
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-3mdv2008.0
+ Revision: 33205
- add macros to %%post and %%postun
- spec file clean

