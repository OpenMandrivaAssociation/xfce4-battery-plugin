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
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.0
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-battery-plugin

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

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libbattery.so
%{_datadir}/xfce4/panel/plugins/battery.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
