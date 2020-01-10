Name:    mallard-rng
Version: 1.0.2
Release: 1%{?dist}
Summary: RELAX NG schemas for all Mallard versions

License: MIT
URL:     http://projectmallard.org/download/
Source0: http://projectmallard.org/download/%{name}-%{version}.tar.bz2

BuildArch:        noarch
Requires(post):   /usr/bin/xmlcatalog
Requires(post):   xml-common
Requires(postun): /usr/bin/xmlcatalog
Requires(postun): xml-common

%description
RELAX NG schemas for all Mallard versions and extensions that have been marked
final.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%post
xmlcatalog --noout --add 'nextCatalog' 'file://%{_sysconfdir}/xml/mallard/catalog' "" %{_sysconfdir}/xml/catalog &> /dev/null || :


%postun
xmlcatalog --noout --del 'file://%{_sysconfdir}/xml/mallard/catalog' %{_sysconfdir}/xml/catalog &> /dev/null || :


%files
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/xml/mallard
%{_datadir}/pkgconfig
%{_sysconfdir}/xml/mallard
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xml/mallard/catalog



%changelog
* Thu Apr 21 2016 David King <amigadave@amigadave.com> - 1.0.2-1
- Initial Fedora packaging (#1264945)
