# revision 18835
# category TLCore
# catalog-ctan /graphics/a2ping/a2ping.pl
# catalog-date 2009-11-09 13:03:38 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-a2ping
Version:	20091109
Release:	1
Summary:	Advanced PS, PDF, EPS converter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/a2ping/a2ping.pl
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a2ping.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a2ping.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-a2ping.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
a2ping is a Perl script command line utility written for Unix
that converts many raster image and vector graphics formats to
EPS or PDF and other page description formats. Accepted input
file formats are: PS (PostScript), EPS, PDF, PNG, JPEG, TIFF,
PNM, BMP, GIF, LBM, XPM, PCX, TGA. Accepted output formats are:
EPS, PCL5, PDF, PDF1, PBM, PGM, PPM, PS, markedEPS, markedPS,
PNG, XWD, BMP, TIFF, JPEG, GIF, XPM. a2ping delegates the low-
level work to Ghostscript (GS), pdftops and sam2p. a2ping fixes
many glitches during the EPS to EPS conversion, so its output
is often more compatible and better embeddable than its input.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/a2ping
%{_texmfdir}/scripts/a2ping/a2ping.pl
%doc %{_mandir}/man1/a2ping.1*
%doc %{_texmfdir}/doc/man/man1/a2ping.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/a2ping/a2ping.pl a2ping
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
