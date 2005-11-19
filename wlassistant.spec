Summary:	Wireless network assistant
Summary(pl):	Asystent sieci bezprzewodowej
Name:		wlassistant
Version:	0.5.4a
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/wlassistant/%{name}-%{version}.tar.bz2
# Source0-md5:	4836d595a27f34c24784cdf9c2a9d5a8
URL:		http://wlassistant.sourceforge.net/
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

%description -l pl
Przyjazny dla u¿ytkownika interfejs KDE pozwalaj±cy wyszukiwaæ i
³±czyæ siê z sieciami bezprzewodowymi przy u¿yciu dowolnego urz±dzenia
obs³uguj±cego rozszerzenia Wireless.

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

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/wlassistant.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/wlassistant.desktop
%{_datadir}/icons/*/*x*/apps/wlassistant.png
