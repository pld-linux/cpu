Summary:	Change Password Utility
Summary(pl):	Narz�dzie do zmiany hase�
Name:		cpu
Version:	1.4.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/cpu/%{name}-%{version}.tar.bz2
# Source0-md5:	2d128f82261967d41458800752bc943d
URL:		http://cpu.sourceforge.net/
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-lbflags.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPU is an LDAP user management tool written in C and loosely based on
FreeBSD's pw(8). The goal of CPU is to be a suitable replacement of
the useradd/usermod/userdel utilities for administrators using an LDAP
backend and wishing to have a suite of command line tools for doing
the administration.

%description -l pl
CPU to narz�dzie do zarz�dzania u�ytkownikami w LDAP, napisane w C i
bazuj�ce na pw(8) z FreeBSD. Celem CPU jest zast�pienie narz�dzi
useradd/usermod/userdel, korzystaj�c z LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ldap \
	--with-cracklib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir="../rpm-doc"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libcpu*.so.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cpu.conf
%{_mandir}/man?/*
