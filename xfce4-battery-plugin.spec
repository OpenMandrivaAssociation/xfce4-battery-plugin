Summary:	Battery monitor plugin for the Xfce panel
Name:		xfce4-battery-plugin
Version:	0.5.0
Release:	%mkrel 8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-battery-plugin
Source0:	%{name}-%{version}.tar.bz2
Patch0:		02_fix-2.6.21.patch
Patch1:		03_lower-acpi-polling.patch
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
%patch0 -p1
%patch1 -p0
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

%post
%update_icon_cahe hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/devices/*
