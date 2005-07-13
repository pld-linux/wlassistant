Summary:	Wireless network assistant
Summary(pl):	Asystent sieci bezprzewodowej
Name:		wlassistant
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications	
Source0:	http://dl.sourceforge.net/wlassistant/%{name}-%{version}.tar.bz2
# Source0-md5:	0e35591ba3df10db215aadedcb92fff3
URL:		http://wlassistant.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
Requires:	dhcpcd
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireless network assistant.

%description -l pl
Asystent sieci bezprzewodowej.

%prep
%setup -q

%build
%{__make} -f Makefile.cvs
%configure \
%if "%{_lib}" == "lib64"
        --enable-libsuffix=64
%endif

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

mkdir $RPM_BUILD_ROOT%{_desktopdir}/
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/wlassistant.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/wlassistant.desktop
%{_datadir}/apps/wlassistant
%{_datadir}/config.kcfg/waconfig.kcfg
%{_datadir}/icons/*/*x*/apps/wlassistant.png
