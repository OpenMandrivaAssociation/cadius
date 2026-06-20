%define snapshot 20260620

Name:		cadius
Version:	1.4.6%{?snapshot:~%{snapshot}}
Release:	1
%if 0%{?snapshot:1}
Source0:	https://github.com/mach-kernel/cadius/archive/refs/heads/master.tar.gz
%else
Source0:	https://github.com/mach-kernel/cadius/archive/%{version}/%{name}-%{version}.tar.gz
%endif
Summary:	Utility for working with Apple II ProDOS disk images
URL:		https://github.com/mach-kernel/cadius
License:	GPL-3.0
Group:		Emulators
BuildRequires:	make

%patchlist
cadius-compile.patch

%description
Utility for working with Apple II ProDOS disk images
such as those found on https://virtualapple.org/

%prep
%autosetup -p1 %{?snapshot:-n %{name}-master}

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_PREFIX=%{_prefix}

%files
%{_bindir}/*
