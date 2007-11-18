Summary:	Battery monitor plugin for the Xfce panel
Name:		xfce-battery-plugin
Version:	0.5.0
Release:	%mkrel 3
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-battery-plugin
Source0:	xfce4-battery-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4.0
BuildRequires:	xfce-panel-devel >= 4.4.0
BuildRequires:	libxfcegui4-devel >= 4.4.0
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Battery monitor panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-battery-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a
rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%find_lang xfce4-battery-plugin

%post
%update_icon_cahe hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-battery-plugin.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/devices/*
