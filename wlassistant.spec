Summary:	Wireless network assistant
Summary(pl.UTF-8):	Asystent sieci bezprzewodowej
Name:		wlassistant
Version:	0.5.7
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/wlassistant/%{name}-%{version}.tar.bz2
# Source0-md5:	4623b498ac42839d08c631c500f18f8b
Patch0:		%{name}-fixkdeconfig.patch
URL:		http://wlassistant.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libiw-devel
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.337
BuildRequires:	scons
BuildRequires:	zlib-devel
Requires:	dhcpcd
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A user friendly KDE frontend allowing you to scan for and connect to
wireless networks using any adapter utilizing Wireless Extensions.

%description -l pl.UTF-8
Przyjazny dla użytkownika interfejs KDE pozwalający wyszukiwać i
łączyć się z sieciami bezprzewodowymi przy użyciu dowolnego urządzenia
obsługującego rozszerzenia Wireless.

%prep
%setup -q
%patch0 -p0

%build
%{__scons} configure \
%if "%{_lib}" == "lib64"
	libsuffix=64 \
%endif
	prefix=%{_prefix} \
	datadir=%{_datadir} \
	qtdir=%{_prefix} \
	kdedir=%{_prefix} \
	kdelibs=%{_libdir} \
	qtlibs=%{_libdir}/qt \
	kdeincludes=%{_includedir} \
	qtincludes=%{_includedir}/qt
%{__scons} .

%install
rm -rf $RPM_BUILD_ROOT

%{__scons} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/wlassistant.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog doc/AUTHORS doc/NEWS doc/README doc/TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/wlassistant.desktop
%{_iconsdir}/*/*x*/apps/wlassistant.png
