#
# Conditional build
%bcond_without  apidocs #disable gtk-doc
#
%define     _packname rest
Summary:	Library for accessing RESTful services
Name:		librest
Version:	0.6.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0:	http://moblin.org/sites/all/files/%{_packname}-%{version}.tar.gz
# Since the projects repository vanished we'll borrow the package from Debian
Source0:	http://ftp.debian.org/debian/pool/main/libr/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	4cd7bb394027ae36b67fdf874898b9fa
URL:		http://moblin.org/projects/librest
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_apidocs:BuildRequires:  gtk-doc >= 1.7}
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library was designed to make it easier to access web services
that claim to be "RESTful". A RESTful service should have urls that
represent remote objects, which methods can then be called on.

It is comprised of two parts: The first aims to make it easier to make
requests by providing a wrapper around libsoup. The second aids with
XML parsing by wrapping libxml2.

%package devel
Summary:	Header files for librest
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for librest.

%package static
Summary:	Static librest library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librest library.

%package apidocs
Summary:        Librest library API documentation
Summary(pl.UTF-8):      Dokumentacja API biblioteki librest.
Group:          Documentation
Requires:       gtk-doc-common

%description apidocs
Librest library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki librest.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{_packname}-0.6/
%dir %{_includedir}/%{_packname}-0.6/%{_packname}
%{_includedir}/%{_packname}-0.6/%{_packname}/*.h
%dir %{_includedir}/%{_packname}-0.6/rest-extras
%dir %{_includedir}/%{_packname}-0.6/rest-extras/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{_packname}-0.6
%endif
