Summary:	Wireless network assistant
Summary(pl.UTF-8):	Asystent sieci bezprzewodowej
Name:		wlassistant
Version:	0.5.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/wlassistant/%{name}-%{version}.tar.bz2
# Source0-md5:	06b767d637e9a2374b07e9e079e2d40d
URL:		http://wlassistant.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libiw-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-devel
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

%build
./configure \
%if "%{_lib}" == "lib64"
        libsuffix=64 \
%endif
	prefix=%{_prefix} \
        datadir=%{_datadir} \
        qtincludes=%{_includedir}/qt

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
