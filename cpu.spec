Summary:	Change Password Utility
Summary(pl):	Narzędzie do zmiany haseł
Name:		cpu
Version:	1.4.3
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://cpu.sourceforge.net/
Source0:	http://dl.sourceforge.net/cpu/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
# Source0-md5:	2d128f82261967d41458800752bc943d
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPU is an LDAP user management tool written in C and loosely based on
FreeBSD's pw(8). The goal of CPU is to be a suitable replacement of
the useradd/usermod/userdel utilities for administrators using an LDAP
backend and wishing to have a suite of command line tools for doing
the administration.

%description -l pl
CPU to narzędzie do zarządzania użytkownikami w LDAP, napisane w C i
bazujące na pw(8) z FreeBSD. Celem CPU jest zastąpienie narzędzi
useradd/usermod/userdel, korzystając z LDAP.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir="../rpm-doc"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libcpu*.so.*.*
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/cpu.conf
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man?/*
