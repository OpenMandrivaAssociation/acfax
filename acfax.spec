Name:         	acfax
Version:      	981011
Summary:      	Amateur Radio FAX Receiving Software for Linux / X11 
Release:      	%mkrel 2
License:        GPLv2+
Group:          Networking/Other
URL:            http://linux.maruhn.com/sec/acfax.html
Group:        	Networking/Other 
Source:       	ftp://ftp.funet.fi/pub/ham/unix/Linux/misc/%{name}-%{version}.tar.gz
Patch0:        	acfax.dif
Patch1:       	widgets.c_missing_sentinel.diff
Patch2:       	acfax_mod_demod_c__fix-includes.diff
Patch3:       	acfax_DirMgr_RE_SYNTAX_EGREP.patch  
BuildRequires:	gccmakedep
BuildRequires:	imake
BuildRequires:	Xaw3d-devel

%description
Software to receive ham radio faxes with the soundcard.

%prep
%setup -q -n acfax
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
xmkmf -a

%make \
	CDEBUGFLAGS="%{optflags}" \
	CXXDEBUGFLAGS="%{optflags}" \
	LOCAL_LDFLAGS="%{ldflags}"


%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc 0* ChangeLog
%{_bindir}/acfax
