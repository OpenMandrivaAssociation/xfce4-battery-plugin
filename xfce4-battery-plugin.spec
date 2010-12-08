Summary:	Battery monitor plugin for the Xfce panel
Name:		xfce4-battery-plugin
Version:	0.5.1
Release:	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch2:		%{name}-0.5.0-fixes-against-kernel-2.6.24.patch
Patch3:		07_use-sysfs-fixed.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-battery-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Battery monitor panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a
rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cahe hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/devices/*
