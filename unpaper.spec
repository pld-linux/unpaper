#
Summary:	Post-processing for scanned and photocopied book pages
Name:		unpaper
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.berlios.de/unpaper/%{name}-%{version}.tar.gz
# Source0-md5:	be41eaf8556e7df39ab53939c99c4f7b
URL:		http://unpaper.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unpaper is a post-processing tool for scanned sheets of paper, especially for
book pages that have been scanned from previously created photocopies. The main
purpose is to make scanned book pages better readable on screen after
conversion to PDF. Additionally, unpaper might be useful to enhance the quality
of scanned pages before performing optical character recognition (OCR). unpaper
tries to clean scanned images by removing dark edges that appeared through
scanning or copying on areas outside the actual page content (e.g. dark areas
between the left-hand-side and the right-hand-side of a double- sided book-page
scan). The program also tries to detect disaligned centering and rotation of
pages and will automatically straighten each page by rotating it to the correct
angle. This process is called "deskewing".

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o unpaper src/unpaper.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install unpaper $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE doc/*
%attr(755,root,root) %{_bindir}/*
