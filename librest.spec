%define     _packname rest
Summary:	Library for accessing RESTful services
Name:		librest
Version:	0.6
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://moblin.org/sites/all/files/%{_packname}-%{version}.tar.gz
# Source0-md5:	8f27683999eeb1de96ca2d955348b578
URL:		http://moblin.org/projects/librest
BuildRequires:	libsoup-gnome-devel
Requires:	libsoup-gnome
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

%prep
%setup -q -n %{_packname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_datadir}/gtk-doc/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{_packname}/
%dir %{_includedir}/%{_packname}/%{_packname}
%{_includedir}/%{_packname}/%{_packname}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
