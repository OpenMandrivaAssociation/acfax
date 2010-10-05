Name:         	acfax
Summary:      	Amateur Radio FAX Receiving Software for Linux / X11 
License:        GPLv2
Group:          Monitoring
URL:            ftp://ftp.funet.fi/pub/ham/unix/Linux/misc/acfax-980709.tar.gz
Group:        	Networking/Other 
Version:      	981011 
Release:      	%mkrel 1
Source:       	acfax-981011.tar.bz2
Patch:        	acfax.dif
Patch1:       	widgets.c_missing_sentinel.diff
Patch2:       	acfax_mod_demod_c__fix-includes.diff
Patch3:       	acfax_DirMgr_RE_SYNTAX_EGREP.patch  
BuildRequires:	imake

%description
Software to receive ham radio faxes with the soundcard.


%prep
%setup -n acfax
%patch
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
xmkmf
make

%install
DOCDIR=/usr/doc/packages/
DOC=""
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc 0FEATURES
%doc 0README
%doc 0TODO
%doc 0Where_to_get
%doc COPYING
%doc ChangeLog
%{_bindir}/acfax


