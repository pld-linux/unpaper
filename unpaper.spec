Summary:	Post-processing for scanned and photocopied book pages
Name:		unpaper
Version:	6.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/Flameeyes/%{name}/archive/%{name}-%{version}.tar.gz
# Source0-md5:	ec5e54d6189773959d509b7c3f3d5c31
URL:		https://www.flameeyes.eu/projects/unpaper
BuildRequires:	ffmpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies. The main purpose is to make scanned book pages
better readable on screen after conversion to PDF. Additionally,
unpaper might be useful to enhance the quality of scanned pages before
performing optical character recognition (OCR). unpaper tries to clean
scanned images by removing dark edges that appeared through scanning
or copying on areas outside the actual page content (e.g. dark areas
between the left-hand-side and the right-hand-side of a double- sided
book-page scan). The program also tries to detect disaligned centering
and rotation of pages and will automatically straighten each page by
rotating it to the correct angle. This process is called "deskewing".

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name} $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/unpaper.1*
